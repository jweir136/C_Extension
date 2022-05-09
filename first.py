import numpy as np
import random
import time

size = 256

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
def python_implementation(arr1, arr2):
    result = np.zeros((len(arr1), len(arr2[0])))

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result

@timer
def numpy_implementation(arr1, arr2):
    return np.dot(arr1, arr2)

if __name__ == "__main__":
    data = generate(size, range_=(1, 100))

    python_time, _ = python_implementation(*data)
    numpy_time, _ = numpy_implementation(*data)

    print(python_time)
    print(numpy_time)