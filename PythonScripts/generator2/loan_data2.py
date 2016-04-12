from datetime import datetime, date
import random


def get_loan(client_id, client_registration_date, cursor):
    loan_name = ('Ипотека', 'Автокредит', 'Потребительский')
    open_date = loan_open_date(client_registration_date)
    period = random.randint(1, 10)
    close_date = loan_close_date(open_date, period)
    rate = random.randint(90, 180)
    rate /= 10
    if close_date is None:
        rest = random.randint(100000, 2000000)
        sql = """
        insert into Loan(loan_name, open_date,
        loan_period, loan_rest, loan_rate, client_id)
        values('{0}','{1}',{2},{3},{4},{5})
        """.format(
            loan_name[random.randint(0, 2)], open_date, period,
            rest, rate, client_id)
    else:
        rest = 0
        sql = """
        insert into Loan(loan_name, open_date, close_date,
        loan_period, loan_rest, loan_rate, client_id)
        values('{0}','{1}','{2}',{3},{4},{5},{6})
        """.format(loan_name[random.randint(0, 2)], open_date,
                   close_date, period, rest, rate, client_id)
    cursor.execute(sql)


def loan_open_date(reg_date):
    year = random.randint(reg_date.year, datetime.today().year)
    if year == datetime.today().year:
        month = random.randint(1, datetime.today().month)
        if month == datetime.today().month:
            day = random.randint(1, datetime.today().day)
            return date(year, month, day)
        else:
            if month in (1, 3, 5, 7, 8, 10, 12):
                day = random.randint(1, 31)
            elif month in (4, 6, 9, 11):
                day = random.randint(1, 30)
            elif month == 2:
                day = random.randint(1, 28)
            return date(year, month, day)
    else:
        month = random.randint(1, 12)
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        elif month == 2:
            day = random.randint(1, 28)
        return date(year, month, day)


def loan_close_date(open_date, period):
    close_date = date(open_date.year + period, open_date.month, open_date.day)
    if close_date > date.today():
        return None
    else:
        return close_date
