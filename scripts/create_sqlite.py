import os
import sqlite3

from dbio3d.utils import array_to_bytes
from dbio3d.mmap import MMapRead
from dbio3d.offset import get_indices_list

from tqdm import tqdm


def create_db(conn):
    cur = conn.cursor()

    create_query = "CREATE TABLE IF NOT EXISTS cubes (id INTEGER PRIMARY KEY AUTOINCREMENT, cube_id INTEGER, idx INTEGER, data BLOB );"
    index_query = "CREATE INDEX IF NOT EXISTS  cubes_idx ON cubes (cube_id, idx)"

    # Création de la table avec une colonne pour un entier et une autre pour un blob (bytes)
    cur.execute(create_query)
    cur.execute(index_query)
    conn.commit()


if __name__ == "__main__":

    root_path = os.path.join(os.path.dirname(__file__), "..", "data")
    # Chemin vers la base de données SQLite
    db_path = os.path.join(root_path, "sqlite3.db")
    n = 50

    os.unlink(db_path)

    # Connexion à la base de données (elle sera créée si elle n'existe pas)
    conn = sqlite3.connect(db_path)

    create_db(conn)

    # Création d'un curseur
    cur = conn.cursor()

    cube_id = 4419
    with MMapRead(root_path) as s_read:
        for idx in tqdm(get_indices_list(n, seed=3)):
            offset, array = s_read.load_cube(cube_id, idx)

            # Conversion du tableau en bytes
            data_bytes = array_to_bytes(array)

            # Insertion des données dans la table
            cur.execute(
                """
            INSERT INTO cubes (cube_id, idx, data) VALUES (?, ?, ?)
            """,
                (cube_id, idx, data_bytes),
            )

    # Validation des changements
    conn.commit()
    conn.close()
