import h5py
from dbio3d.offset import hash_to_offset
from dbio3d.reader import Reader


class Hdf5Read(Reader):

    def __init__(self, db_path: str) -> None:
        super().__init__(db_path=db_path)
        self.hdf5 = None

    def __enter__(self):
        self.hdf5 = h5py.File(self.db_path, "r")
        return self

    def load_cube(self, cube_id, idx):
        dset = self.hdf5[f"{cube_id}/{idx}"]
        # Easy to add attributes
        # print(dset.attrs["permeability"])
        array = dset[:]
        return hash_to_offset(idx), array

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.hdf5.close()
