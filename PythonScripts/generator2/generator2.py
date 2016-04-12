from generator2.branch_data2 import get_address, get_branch
from generator2.client_data2 import get_client, get_client_addresses
from generator2.client_data2 import get_female_name, get_male_name
import random
import MySQLdb


def filter_data(db, cursor):
    try:
        cursor.execute("""
            create view Passport(id,pass, col) as select client_id, person_passport,
            count(*) from Person group by(person_passport)""")
        db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()
    try:
        cursor.execute("""
            create view Passport_clear(id_c) as select id from Passport where col>1""")
        db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()
    try:
        cursor.execute("""
           select id_c from Passport_clear""")
    except MySQLdb.Error as error:
        print(error)
        db.rollback()
    try:
        clients = []
        condition = None
        for i in range(cursor.rowcount):
            clients.append(cursor.fetchone()[0])
        if len(clients) != 0:
            if len(clients) > 1:
                client = tuple(clients)
                condition = "in " + str(client)
            else:
                client = clients[0]
                condition = "= " + str(client)

            cursor.execute(
                """delete from Person where client_id {0}""".format(condition))
            cursor.execute(
                """delete from Account where client_id {0}""".format(condition))
            cursor.execute(
                """delete from Loan where client_id {0}""".format(condition))
            cursor.execute(
                """delete from Client where client_id {0}""".format(condition))
            db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()


def generator2(min_c, max_c):
    db = MySQLdb.connect(host="localhost", user="root",
                         passwd="", db="Bank_OLTP", charset='utf8')
    cursor = db.cursor()
    branches = get_address()
    names = (get_male_name(), get_female_name())
    genders = ("Мужской", "Женский")
    client_addresses = get_client_addresses()
    passport_series = {"Москва": '45', "Санкт-Петербург": '40',
                       "Ростов-на-Дону": '60',
                       "Нижний Новгород": '22', "Казань": '92',
                       "Екатеринбург": '65',
                       "Новосибирск": '50', "Владивосток": '05'}
    branch_id = 1
    client_id = 1
    for city, streets in branches.items():
        for street in streets:
            get_branch(branch_id, city, street, cursor)
            cursor.execute("start transaction")
            client_id = get_client(client_id, branch_id,
                                   random.randint(min_c, max_c),
                                   names, genders, city,
                                   client_addresses[city],
                                   passport_series[city], cursor)
            branch_id += 1
            cursor.execute("commit")
    db.commit()
    filter_data(db, cursor)
    cursor.execute("""select count(*) from Client""")
    client_id = cursor.fetchone()[0]
    db.close()
    print(client_id)
    return client_id
