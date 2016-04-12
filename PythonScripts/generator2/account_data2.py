import random


def get_account(flag, branch_id, client_id, cursor):
    if flag == 0:
        balance = random.randint(1000000, 10000000)
    else:
        balance = random.randint(50000000, 500000000)
    num = random.randint(100, 200)
    balance /= num
    rate = random.randint(90, 180)
    rate /= 10
    account_type = "Депозит"
    status = "Открыт"
    sql = """
    insert into Account(balance,rate, account_type,
    status,client_id, branch_id) values(
    {0},{1},'{2}','{3}',{4},{5})
    """.format(balance, rate, account_type, status,
               client_id, branch_id)
    cursor.execute(sql)
