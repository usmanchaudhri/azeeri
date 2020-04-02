"""
Best practice to use Python threading only in cases of IO bound operations and the reason for that the Global Interpreter Lock (GIL).

GIL - a lock that prevents multiple native threads from executing Python code at the same time. GIL prevents thread interference and race conditions.
Help the python code integrate with C libraries which aren't thread safe either.

In Python there is Cooperative multi-threading where each thread uses the same CPU core - time multiplexing.

GIL workarounds - is to use a python interpreter which does not uses GIL i.e Jython or IronPython
GIL workarounds - using Python multiprocessing module
"""

