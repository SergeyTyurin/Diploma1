import matplotlib.pyplot as plt
import csv

if __name__ == '__main__':
    f = open("analyze2.csv", "r")
    info = [[], []]
    lines = csv.reader(f, delimiter=' ')
    for line in lines:
        print(line)
        info[0].append(line[0])
        info[1].append(line[1])
    f.close()
    plt.xlabel(u'Число клиентов')
    plt.ylabel(u"""Время заполнения, с""")
    plt.plot(info[0], info[1], label=u'Время заполнения')
    plt.grid(True)
    plt.legend(loc='best', frameon=True)
    plt.show()
