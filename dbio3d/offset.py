import numpy as np


def _get_offset(shape=(2800, 1100, 1100), dim=100):
    return [int(np.random.choice(range(0, shape[i] - dim))) for i in [0, 1, 2]]

def hash_to_offset(index, shape=(2800, 1100, 1100)):
    val = index // shape[0]
    i = index % shape[0]
    j = val // shape[1]
    k = val % shape[1]
    return i, j, k

def offset_to_hash(offset, shape=(2800, 1100, 1100)):
    return offset[0] + (offset[1]*shape[1] + offset[2])*shape[0]

def get_indices_list(n, seed=None):
    offsets = set()
    if seed is not None:
        np.random.seed(seed)
    
    while (len(offsets)<n):
        offset = _get_offset()
        offsets.add(offset_to_hash(offset))

    return list(offsets)

if __name__ == "__main__":
    offset = _get_offset()
    index = offset_to_hash(offset)
    offset_restored = hash_to_offset(index)
    print(offset, index , offset_restored )
    for h in get_indices_list(10, seed=3):
        print(hash_to_offset(h))