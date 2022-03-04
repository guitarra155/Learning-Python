from ctypes.wintypes import PINT


def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i-1)

recursion(7)
