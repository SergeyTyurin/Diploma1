import random
import json
from datetime import datetime, date
from generator2.text_transformation import street_filter
from generator2.account_data2 import get_account
from generator2.loan_data2 import get_loan
import os
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_client_addresses():
    dict = {}
    try:
        f = open(dir_name + "/TextData/cities_streets.json", 'r')
        dict = json.loads(f.read())
        f.close()
        for city, streets in dict.items():
            streets = street_filter(streets)
        return dict
    except Exception as error:
        print(error)
        f.close()
        return None


def get_client(client_id, branch_id, number, names, genders, city, streets,
               passport_series, cursor):
    j = client_id
    for i in range(j, j + number + 1):
        #cursor.execute("start transaction")
        if client_id % 500 == 0:
            get_organization(client_id, 'Организация' + str(round(client_id / 500)),
                             get_foundation_org_date(), cursor)
            get_account(1, branch_id, client_id, cursor)
        else:
            g = random.randint(0, 1)
            get_person(i, names[g][0][random.randint(0, len(names[g][0]) - 1)],
                       names[g][1][random.randint(0, len(names[g][1]) - 1)],
                       genders[g], city, streets, passport_series, cursor)
            get_account(0, branch_id, client_id, cursor)
        client_id += 1
        # cursor.execute("commit")
    return client_id


def get_birthday():
    year = datetime.today().year - random.randint(20, 60)
    month = random.randint(1, 12)
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 31)
    elif month in (4, 6, 9, 11):
        day = random.randint(1, 30)
    elif month == 2:
        day = random.randint(1, 28)
    return date(year, month, day)


def get_registration_date(birthday):
    reg = birthday.year + 20
    if reg < 1991:
        reg = 1991
    if reg != datetime.today().year:
        year = random.randint(reg, datetime.today().year - 1)
    else:
        year = datetime.today().year
    month = random.randint(1, 12)
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 31)
    elif month in (4, 6, 9, 11):
        day = random.randint(1, 30)
    elif month == 2:
        day = random.randint(1, 28)
    return date(year, month, day)


def get_registration_org_date(foundation):
    year = random.randint(foundation.year, datetime.today().year)
    month = random.randint(1, 12)
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 31)
    elif month in (4, 6, 9, 11):
        day = random.randint(1, 30)
    elif month == 2:
        day = random.randint(1, 28)
    return date(year, month, day)


def get_foundation_org_date():
    year = random.randint(1991, datetime.today().year - 1)
    month = random.randint(1, 12)
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 31)
    elif month in (4, 6, 9, 11):
        day = random.randint(1, 30)
    elif month == 2:
        day = random.randint(1, 28)
    return date(year, month, day)


def get_passport_data(series, year):
    if datetime.today().year - year < 40:
        p_year = year + 20
    else:
        p_year = year + 40
    if p_year < 2000:
        p_year -= 1900
    else:
        p_year -= 2000
    series += str(p_year).zfill(2)
    number = random.randint(100000, 999999)
    return series + ' ' + str(number)


def get_person(client_id, name, second_name, gender, city, streets,
               passport_series, cursor):
    birthday = get_birthday()
    registration_date = get_registration_date(birthday)
    passport = get_passport_data(passport_series, birthday.year)

    sql = """insert into Client values({0}, '{1}')""".format(client_id,
                                                             registration_date)
    cursor.execute(sql)

    sql = """insert into Person(person_name, person_birthday, person_gender,
            person_address, person_passport, client_id)
            values('{0}','{1}','{2}','{3}','{4}',{5})""".format(
        second_name + ' ' + name,
        birthday, gender,
        city + ', ' +
        streets[random.randint(
            0, len(streets) - 1)],
        passport, client_id)
    cursor.execute(sql)
    l = random.randint(0, 9)
    if l <= 4:
        #cursor.execute("start transaction")
        get_loan(client_id, registration_date, cursor)


def get_organization(client_id, name, foundation, cursor):
    ogrn = ''
    for i in range(13):
        ogrn += str(random.randint(0, 9))
    inn = ''
    for i in range(10):
        inn += str(random.randint(0, 9))
    registration_date = get_registration_org_date(foundation)
    sql = """insert into Client values({0}, '{1}')""".format(client_id,
                                                             registration_date)

    cursor.execute(sql)

    sql = """insert into Organization(org_name, org_ogrn, org_inn,
    foundation_date, client_id) values('{0}','{1}','{2}','{3}',{4})""".format(
        name, ogrn, inn, foundation, client_id)

    cursor.execute(sql)


def get_male_name():
    try:
        f_names = open(dir_name + "/TextData/Male_names.txt", 'r')
        f_second_names = open(
            dir_name + "/TextData/Male_second_names.txt", 'r')
        names = f_names.read().strip('\n').split('\n')
        second_names = f_second_names.read().strip('\n').split('\n')
        f_names.close()
        f_second_names.close()
        return (names, second_names)
    except:
        print("Error")
        return None


def get_female_name():
    try:
        f_names = open(dir_name + "/TextData/Female_names.txt", 'r')
        f_second_names = open(
            dir_name + "/TextData/Female_second_names.txt", 'r')
        names = f_names.read().strip('\n').split('\n')
        second_names = f_second_names.read().strip('\n').split('\n')
        f_names.close()
        f_second_names.close()
        return (names, second_names)
    except:
        print("Error")
        return None
