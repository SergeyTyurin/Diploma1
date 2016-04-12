import json
import os
from generator.text_transformation import street_filter
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_address():
    dict = {}
    try:
        f = open(dir_name + "/TextData/branch_address.json", 'r')
        dict = json.loads(f.read())
        f.close()
        for city, streets in dict.items():
            streets = street_filter(streets)
        return dict
    except Exception as error:
        print(error)
        f.close()
        return None


def get_branch(branch_id, city, street, branch_values, f1):
    sql = ("INSERT INTO Branch(branch_id, branch_city, branch_address)\n" +
           "VALUES({0},'{1}','{2}');\n\n").format(branch_id, city, street)
    f1.write(sql)
    branch_values.append((branch_id, city, street))
