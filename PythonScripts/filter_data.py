import MySQLdb


def filter_data(db, cursor):
    try:
        cursor.execute("""
            CREATE VIEW Passport(id,pass, col) AS SELECT client_id, person_passport,
            COUNT(*) FROM Person GROUP BY(person_passport)""")
        db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()
    try:
        cursor.execute("""
            CREATE VIEW Passport_clear(id_c) AS SELECT id FROM Passport WHERE col>1""")
        db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()
    try:
        cursor.execute("""
           SELECT id_c FROM Passport_clear""")
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
            cursor.execute("""CREATE TRIGGER `Delete_Person` BEFORE DELETE ON `Person`
            FOR EACH ROW BEGIN
            DELETE FROM Log WHERE c_id = OLD.`client_id`;
            END;""")
            cursor.execute("""CREATE TRIGGER `Delete_Account` BEFORE DELETE ON `Account`
            FOR EACH ROW BEGIN
            DELETE FROM Log WHERE c_id = OLD.`client_id`;
            END;""")
            cursor.execute("""CREATE TRIGGER `Delete_Loan` BEFORE DELETE ON `Loan`
            FOR EACH ROW BEGIN
            DELETE FROM Log WHERE c_id = OLD.`client_id`;
            END;""")
            cursor.execute(
                """DELETE FROM Person WHERE client_id {0}""".format(condition))
            cursor.execute(
                """DELETE FROM Account WHERE client_id {0}""".format(condition))
            cursor.execute(
                """DELETE FROM Loan WHERE client_id {0}""".format(condition))
            cursor.execute(
                """DELETE FROM Client WHERE client_id {0}""".format(condition))
            cursor.execute("""DROP TRIGGER IF EXISTS `Delete_Person""")
            cursor.execute("""DROP TRIGGER IF EXISTS `Delete_Account""")
            cursor.execute("""DROP TRIGGER IF EXISTS `Delete_Loan""")
        db.commit()
    except MySQLdb.Error as error:
        print(error)
        db.rollback()

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host="localhost", user="root",
                             passwd="", db="Bank_OLTP", charset='utf8')
        cursor = db.cursor()
        filter_data(db, cursor)
        cursor.close()
        db.close()
    except Exception as error:
        print(error)
