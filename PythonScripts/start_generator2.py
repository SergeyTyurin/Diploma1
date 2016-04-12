import sys
import time
from generator2.generator2 import generator2

if __name__ == '__main__':
    try:
        min_c = 2
        max_c = 3
        i = int(sys.argv[1])
        start = time.clock()
        generator2(min_c * i, max_c * i)
        stop = time.clock()
        print("Time", stop - start)
    except Exception as error:
        print(error)
