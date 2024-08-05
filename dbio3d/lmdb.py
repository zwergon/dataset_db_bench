import lmdb

from dbio3d.utils import bytes_to_array
from dbio3d.offset import hash_to_offset
from dbio3d.reader import Reader


class LmdbRead(Reader):

    def __init__(self, db_path: str) -> None:
        super().__init__(db_path=db_path)

    def __enter__(self):
        self.env = lmdb.open(self.db_path, readonly=True)
        return self

    def load_cube(self, cube_id, idx):
        with self.env.begin() as txn:
            cube_data = txn.get(f"{cube_id}/{idx}".encode())
            return hash_to_offset(idx), bytes_to_array(cube_data)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.env.close()
