from multiprocessing import multiprocessing as mp
from math import cos

def pickle_range():
    p = mp.Pool(2)
    res = p.map(cos, range(10))
    print(res)

def pickle_fails_with_lambda_functions():
    p = mp.Pool(2)
    p.map(lambda x: 2**x, range(10))

if __name__ == "__main__":
    pickle_range()
    # pickle_fails_with_lambda_functions()