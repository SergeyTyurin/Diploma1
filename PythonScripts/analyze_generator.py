from generator.generator import generator
from generator2.generator2 import generator2
from truncate_data import main
import time
import math
import sys


def average(times, clients, num):
    avg_time = []
    avg_client = []
    for i in range(len(times[0])):
        s_t = 0.0
        s_c = 0.0
        for j in range(num):
            s_t += times[j][i]**2
            s_c += clients[j][i]**2
        s_t /= num
        s_c /= num
        avg_time.append(math.sqrt(s_t))
        avg_client.append(math.sqrt(s_c))
    return (avg_client, avg_time)


def analyze1():
    min_c = 2
    max_c = 3
    times = []
    clients = []
    for num in range(0, 5):
        clients.append([])
        times.append([])
        for i in (1, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000):
            start = time.clock()
            client_num = generator(min_c * i, max_c * i)
            stop = time.clock()
            clients[num].append(client_num)
            times[num].append(stop - start)
            print(stop - start)
            main()
    info = average(times, clients, num)
    f = open("analyze.csv", "w")
    for i in range(len(info[0])):
        f.write(str(info[0][i]) + ' ' + str(info[1][i]) + '\n')
    f.close()


def analyze2():
    min_c = 2
    max_c = 3
    times = []
    clients = []
    for num in range(0, 5):
        clients.append([])
        times.append([])
        for i in (1, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000):
            start = time.clock()
            client_num = generator2(min_c * i, max_c * i)
            stop = time.clock()
            clients[num].append(client_num)
            times[num].append(stop - start)
            print(stop - start)
            main()
    info = average(times, clients, num)
    f = open("analyze2.csv", "w")
    for i in range(len(info[0])):
        f.write(str(info[0][i]) + ' ' + str(info[1][i]) + '\n')
    f.close()


if __name__ == '__main__':
    if(int(sys.argv[1]) == 1):
        analyze1()
    else:
        analyze2()
