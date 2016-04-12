from generator.branch_data import get_address, get_branch
from generator.client_data import get_client, get_client_addresses
from generator.client_data import get_female_name, get_male_name
import random
import MySQLdb
import sys
import _mysql


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


def dumpfile(client_values, person_values, org_values, branch_values,
             loan_values, account_values, payment_values, f):
    f.write('SET AUTOCOMMIT=0;\nSET FOREIGN_KEY_CHECKS=0;\n')
    val = ""
    for value in branch_values:
        val += str(value) + ',\n'
    f.write("""INSERT INTO Branch VALUES {0};\n""".format(val[:-2]))
    f.write('\n\n\n')
    val = ""
    for value in client_values:
        val += str(value) + ',\n'
    f.write("""INSERT INTO Client VALUES{0};\n""".format(val[:-2]))
    f.write('\n\n\n')
    val = ""
    for value in person_values:
        val += str(value) + ',\n'
    f.write("""INSERT INTO Person(person_name, person_birthday, person_gender,
        person_address, person_passport,client_id)
        VALUES{0};\n""".format(val[:-2]))
    f.write('\n\n\n')
    if org_values:
        val = ""
        for value in org_values:
            val += str(value) + ',\n'
        f.write("""INSERT INTO Organization(org_name, org_ogrn, org_inn,
            foundation_date,client_id) VALUES{0};\n""".format(val[:-2]))
        f.write('\n\n\n')
    val = ""
    for value in account_values:
        val += str(value) + ',\n'
    f.write("""INSERT INTO Account(balance, rate, account_type,
        status, client_id, branch_id) VALUES{0};\n""".format(val[:-2]))
    f.write('\n\n\n')
    val = ""
    for value in loan_values:
        val += "("
        l = 1
        for a in value:
            if a is None:
                val += _mysql.NULL + ','
            elif l == len(value):
                val += repr(a)
            else:
                val += repr(a) + ','
            l += 1
        val += '),\n'
    f.write("""INSERT INTO Loan(loan_name, open_date, close_date,
        loan_period, loan_rest, loan_rate, client_id)
        VALUES{0};\n""".format(val[:-2]))
    f.write('\n\n\n')
    val = ""
    for value in payment_values:
        val += str(value) + ',\n'
    f.write("""INSERT INTO Payment VALUES {0};\n""".format(val[:-2]))
    f.write('\n\n\n')
    f.write('SET AUTOCOMMIT=1;\nSET FOREIGN_KEY_CHECKS=1;\n')


def generator(min_c, max_c, f, f1):
    client_values = []
    person_values = []
    org_values = []
    branch_values = []
    loan_values = []
    account_values = []
    payment_values = []

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
            get_branch(branch_id, city, street, branch_values, f1)
            client_id = get_client(client_id, branch_id,
                                   random.randint(min_c, max_c),
                                   names, genders, city,
                                   client_addresses[city],
                                   passport_series[city], client_values,
                                   person_values, org_values,
                                   loan_values, account_values, payment_values,
                                   f1)
            branch_id += 1
    dumpfile(client_values, person_values, org_values, branch_values,
             loan_values, account_values, payment_values, f)


if __name__ == '__main__':
    min_c = 2
    max_c = 3
    try:
        i = int(sys.argv[1])
        generator(min_c * i, max_c * i)

    except Exception as error:
        print(error)
