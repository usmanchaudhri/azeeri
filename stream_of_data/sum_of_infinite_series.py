"""
Sum of infinite series
"""
import itertools

def running_sum(s, n):
    while True:
        r, s = itertools.tee(s)
        yield sum(itertools.islice(r, n))
        s.next()


running_sum()