
import os

from dbio3d.offset import hash_to_offset
from dbio3d.reader import Reader
from dbio3d.memmap import load_cube, DataModality

class MMapRead(Reader):

    def __init__(self, db_path: str, dim=100) -> None:
        super().__init__(db_path=db_path)
        self.dim = dim

    def load_cube(self, cube_id, idx):
        offset = hash_to_offset(idx)

        return offset, load_cube(
            os.path.join(self.db_path, str(cube_id)),
            DataModality.GLV,
            offset=offset,
            subshape=[self.dim, self.dim, self.dim],
    )
