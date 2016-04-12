import random


def get_account(flag, branch_id, client_id, account_values, f1):  # cursor):
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
    sql = ("INSERT INTO Account(balance,rate," +
           " account_type,status, client_id, branch_id)\n" +
           "VALUES({0},{1},'{2}','{3}',{4},{5});\n").format(
        balance, rate, account_type, status,
        client_id, branch_id)
    f1.write(sql)
    account_values.append((balance, rate,
                           account_type, status,
                           client_id, branch_id))
