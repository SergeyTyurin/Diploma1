from datetime import datetime, date
import random


def get_payment(client_id, client_registration_date, payment_values, f1):
    payment_type = ("Оплата услуг ЖКХ",
                    "Оплата мобильной связи", "Использование карты",
                    "Пополнение счета", "Снятие средств со счета")
    dict_payment_type = {"Платеж по кредиту": random.randint(5000, 25000),
                         "Оплата услуг ЖКХ": random.randint(500, 10000),
                         "Оплата мобильной связи": random.randint(100, 5000),
                         "Использование карты": random.randint(500, 3000),
                         "Пополнение счета": random.randint(100, 1000),
                         "Снятие средств со счета": random.randint(5000, 20000)}
    for p_year in range(client_registration_date.year, datetime.today().year + 1):
        if p_year == client_registration_date.year:
            for month in range(client_registration_date.month, 13):
                random_list = [0, 1, 2, 3, 4]
                jkh = False
                mobile = False
                for j in range(0, random.randint(1, 17)):
                    if(month == client_registration_date.month):
                        if month in (1, 3, 5, 7, 8, 10, 12):
                            day = random.randint(
                                client_registration_date.day, 31)
                        elif month in (4, 6, 9, 11):
                            day = random.randint(
                                client_registration_date.day, 30)
                        elif month == 2:
                            day = random.randint(
                                client_registration_date.day, 28)
                        if(jkh):
                            random_list.remove(0)
                            jkh = False
                        if(mobile):
                            random_list.remove(1)
                            mobile = False

                        p_index = random.choice(random_list)
                        if(p_index == 0):
                            jkh = True
                        if(p_index == 1):
                            mobile = True
                        sql = """insert into Payments(
                        payment_type, payment_value, payment_date, client_id)
                        values('{0}',{1},'{2}',{3})""".format(
                            payment_type[p_index],
                            dict_payment_type[payment_type[p_index]],
                            date(p_year, month, day), client_id)
                        f1.write(sql)
                        payment_values.append([payment_type[p_index],
                                               dict_payment_type[
                            payment_type[p_index]],
                            date(p_year, month, day),
                            client_id])
                    else:
                        if month in (1, 3, 5, 7, 8, 10, 12):
                            day = random.randint(1, 31)
                        elif month in (4, 6, 9, 11):
                            day = random.randint(1, 30)
                        elif month == 2:
                            day = random.randint(1, 28)

                        if(jkh):
                            random_list.remove(0)
                            jkh = False
                        if(mobile):
                            random_list.remove(1)
                            mobile = False

                        p_index = random.choice(random_list)
                        if(p_index == 0):
                            jkh = True
                        if(p_index == 1):
                            mobile = True
                        sql = """insert into Payments(
                        payment_type, payment_value, payment_date, client_id)
                        values('{0}',{1},'{2}',{3})""".format(
                            payment_type[p_index],
                            dict_payment_type[payment_type[p_index]],
                            date(p_year, month, day), client_id)
                        f1.write(sql)
                        payment_values.append([payment_type[p_index],
                                               dict_payment_type[
                            payment_type[p_index]],
                            date(p_year, month, day),
                            client_id])
        else:
            for month in range(1, 12):
                random_list = [0, 1, 2, 3, 4]
                jkh = False
                mobile = False
                for j in range(0, random.randint(1, 17)):
                    if month in (1, 3, 5, 7, 8, 10, 12):
                        day = random.randint(1, 31)
                    elif month in (4, 6, 9, 11):
                        day = random.randint(1, 30)
                    elif month == 2:
                        day = random.randint(1, 28)

                    if(jkh):
                        random_list.remove(0)
                        jkh = False
                    if(mobile):
                        random_list.remove(1)
                        mobile = False

                    p_index = random.choice(random_list)
                    if(p_index == 0):
                        jkh = True
                    if(p_index == 1):
                        mobile = True
                    sql = """insert into Payments(
                        payment_type, payment_value, payment_date, client_id)
                        values('{0}',{1},'{2}',{3})""".format(
                        payment_type[p_index],
                        dict_payment_type[payment_type[p_index]],
                        date(p_year, month, day), client_id)
                    f1.write(sql)
                    payment_values.append([payment_type[p_index],
                                           dict_payment_type[
                        payment_type[p_index]],
                        date(p_year, month, day), client_id])
