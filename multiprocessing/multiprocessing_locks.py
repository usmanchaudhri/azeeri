from __future__ import with_statement

import multiprocessing
import threading
import time

"""
deposit and withdraw functions without locks
"""
lock = threading.Lock()

# def deposit(balance):
#     for i in range(500):
#         time.sleep(0.1)
#         balance.value = balance.value + 1
#
# def withdraw(balance):
#     for i in range(500):
#         time.sleep(0.1)
#         balance.value = balance.value - 1

"""
deposit and withdraw functions with locks
"""
def deposit(balance):
    for i in range(500):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance):
    for i in range(500):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('i', 500)
    p1 = multiprocessing.Process(target=deposit, args=(balance,))
    p2 = multiprocessing.Process(target=withdraw, args=(balance,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(balance.value)
