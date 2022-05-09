import c_extension

import numpy as np
import random
import time

size = 500

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        return time.time() - before, result

    return wrapper

def generate(size, range_):
    arr = [[[random.randrange(*range_) for _ in range(size)] for _ in range(size)] for _ in range(2)]
    return arr

@timer
def my_implementation(arr1, arr2):
    return c_extension.dot_product_optimized_parallel(arr1, arr2)

@timer
def numpy_implementation(arr1, arr2):
    return np.dot(arr1, arr2)

if __name__ == "__main__":
    data = generate(size, range_=(1, 100))

    python_time, _ = my_implementation(*data)
    numpy_time, _ = numpy_implementation(*data)

    print(python_time)
    print(numpy_time)