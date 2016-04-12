import re
countries = ("moscow_streets.txt",
             "st-peterburg_streets.txt",
             "rostov_streets.txt",
             "novgorod_streets.txt",
             "kazan_streets.txt",
             "ekaterinburg_streets.txt",
             "novosibirsk_streets.txt",
             "vladivostok_streets.txt")
try:
    for city in countries:
        f = open(city, "r")
        lines = f.readlines()
        streets = []
        for i in range(len(lines)):
            lines[i] = re.sub(r'[,\n]', '', lines[i])
            lines[i] = '\"' + lines[i] + '\"'
            streets.append(lines[i])
            # print(lines[i])
        f.close()
        f = f = open(city, "w")
        for i in range(len(streets)):
            f.write(streets[i] + ',\n')
        f.close()
except Exception as error:
    print(error)
    f.close()
