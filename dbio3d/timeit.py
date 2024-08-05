import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        
        print(f"{func.__name__} - Elapsed time: ", elapsed_time)
    return wrapper