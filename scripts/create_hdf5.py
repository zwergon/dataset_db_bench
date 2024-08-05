import os
import h5py
from dbio3d.mmap import MMapRead
from dbio3d.offset import get_indices_list
from tqdm import tqdm
import numpy as np


if __name__ == "__main__":

    root_path = os.path.join(os.path.dirname(__file__), "..", "data")
    # Chemin vers la base de données SQLite
    h5split_path = os.path.join(root_path, "split.hdf5")
    n = 50

    os.unlink(h5split_path)

    with h5py.File(h5split_path, "w") as h5file:
        with MMapRead(root_path) as s_read:
            cube_id = 4419
            for idx in tqdm(get_indices_list(n, seed=3)):
                offset, array = s_read.load_cube(cube_id, idx)
                group_name = str(cube_id)

                group = h5file.require_group(group_name)
                offset, array = s_read.load_cube(cube_id, idx)
                dset = group.create_dataset(str(idx), data=array)
                dset.attrs["permeability"] = np.random.normal(loc=1e-3, scale=1e-4)

    print(array.shape, offset)

    # with h5py.File(h5split_path, 'w') as h5file:
    #
