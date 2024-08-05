import os

import numpy as np
from dbio3d.timeit import timeit

from dbio3d.offset import get_indices_list

from dbio3d import Reader, create_reader


@timeit
def load_cubes(s_read: Reader, indices):

    print(f"load {len(indices)} cubes with {s_read.__class__.__qualname__}")
    for idx in indices:
        offset, cube = s_read.load_cube(4419, idx)

    print(offset, cube.shape)


if __name__ == "__main__":

    root_path = os.path.join(os.path.dirname(__file__), "..", "data")

    path_map = {
        "mmap": os.path.join(root_path),
        "sqlite": os.path.join(root_path, "sqlite3.db"),
        "hdf5": os.path.join(root_path, "split.hdf5"),
        "lmdb": os.path.join(root_path, "dataset.lmdb"),
    }

    key = "hdf5"

    indices = get_indices_list(50, seed=3)

    with create_reader(key, path_map[key]) as s_read:
        load_cubes(s_read, indices)
