from .reader import Reader
from .mmap import MMapRead
from .hdf5 import Hdf5Read
from .sqlite import SqliteRead
from .lmdb import LmdbRead


def create_reader(name: str, db_path: str) -> Reader:

    return {
        "mmap": MMapRead,
        "hdf5": Hdf5Read,
        # "zhdf5": Hdf5Read,
        "sqlite": SqliteRead,
        "lmdb": LmdbRead,
    }[name](db_path)
