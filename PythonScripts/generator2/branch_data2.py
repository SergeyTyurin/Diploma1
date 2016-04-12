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


def get_branch(branch_id, city, street, cursor):
    sql = """insert into Branch(branch_id, branch_city, branch_address)
    values({0},'{1}','{2}')""".format(branch_id, city, street)
    # print(sql)
    cursor.execute(sql)
