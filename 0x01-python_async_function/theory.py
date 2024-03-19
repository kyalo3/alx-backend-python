from random import randint
import time
import asyncio


def odds(start, stop):
    """generator function(odds)"""
    for odd in range(start, stop + 1, 2):
        """used to pause and resume the fucntion"""
        yield odd

def randn():
    """randn function to illustrate coroutines"""
    time.sleep(3)
    return randint(1, 10)

def main():
    """returns the diff lists"""
    odds1 = [odd for odd in odds(3, 45)]
    odds2 = tuple(odds(21, 45))
    print(odds1)
    print(odds2)

if __name__ == "__main__":
    main()
