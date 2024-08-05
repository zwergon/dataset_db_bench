import os
import lmdb
from dbio3d.utils import array_to_bytes
from dbio3d.mmap import MMapRead
from dbio3d.offset import get_indices_list
from tqdm import tqdm

import numpy as np

if __name__ == "__main__":

    root_path = os.path.join(os.path.dirname(__file__), "..", "data")
    # Chemin vers la base de données SQLite
    db_path = os.path.join(root_path, "dataset.lmdb")
    n = 50

    os.makedirs(db_path)

    env = lmdb.open(db_path, map_size=int(1.1 * 2000000 * 50))
    with env.begin(write=True) as txn:
        with MMapRead(root_path) as s_read:
            cube_id = 4419
            for idx in tqdm(get_indices_list(n, seed=3)):
                offset, array = s_read.load_cube(cube_id, idx)
                cube_data = array_to_bytes(array)
                txn.put(f"{cube_id}/{idx}".encode(), cube_data)

    print(array.shape, offset)

    # with h5py.File(h5split_path, 'w') as h5file:
    #
