import msgpack_numpy as m


# Fonction pour convertir un tableau NumPy en bytes
def array_to_bytes(arr):
    return m.dumps(arr)


def bytes_to_array(barray):
    return m.loads(barray)
