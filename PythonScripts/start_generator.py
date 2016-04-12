import sys
import time
from generator.generator import generator

if __name__ == '__main__':
    min_c = 2
    max_c = 3
    i = int(sys.argv[1])
    f = open("bank_data_" + str(i) + ".sql", "w")
    f1 = open("bank_data_" + str(i) + "_1.sql", "w")
    start = time.clock()
    generator(min_c * i, max_c * i, f, f1)
    f1.close()
    f.close()
    stop = time.clock()
    print("Time", stop - start)
    # except Exception as error:
    #    print(error)
