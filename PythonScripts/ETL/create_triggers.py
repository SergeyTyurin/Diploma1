import MySQLdb


def create_triggers(db):
    try:
        cur = db.cursor()
        sql = """CREATE TRIGGER `Insert_Person` AFTER INSERT ON `Person`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('INSERT','Person',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Update_Person` AFTER UPDATE ON `Person`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('UPDATE','Person',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Insert_Organization` AFTER INSERT ON `Organization`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('INSERT','Organization',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Update_Organization` AFTER UPDATE ON `Organization`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('UPDATE','Organization',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Insert_Account` AFTER INSERT ON `Account`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('INSERT','Account',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Update_Account` AFTER UPDATE ON `Account`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('UPDATE','Account',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Insert_Loan` AFTER INSERT ON `Loan`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('INSERT','Loan',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        sql = """CREATE TRIGGER `Update_Loan` AFTER UPDATE ON `Loan`
            FOR EACH ROW BEGIN
            INSERT INTO Log(req_type, log_table, c_id)
            VALUES('UPDATE','Loan',NEW.`client_id`);
            END;"""
        cur.execute(sql)
        db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host='localhost', user='root',
                             db='Bank_OLTP', charset='utf8')
    except MySQLdb.Error as error:
        print(error)
    else:
        create_triggers(db)
