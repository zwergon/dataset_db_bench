import sqlite3

from dbio3d.utils import bytes_to_array
from dbio3d.offset import hash_to_offset
from dbio3d.reader import Reader


class SqliteRead(Reader):

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self

    def load_cube(self, cube_id, idx):
        cur = self.conn.cursor()
        # # Exemple de lecture des données
        cur.execute(f"SELECT data FROM cubes where cube_id={cube_id} and idx={idx}")
        row = cur.fetchone()

        return hash_to_offset(idx), bytes_to_array(row[0])

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()
