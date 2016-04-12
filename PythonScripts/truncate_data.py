import MySQLdb


def main():
    db = MySQLdb.connect(host="localhost", user="root",
                         passwd="", db="Bank_OLTP", charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute("""SET FOREIGN_KEY_CHECKS = 0""")
        cursor.execute("""TRUNCATE Loan""")
        cursor.execute("""TRUNCATE Account""")
        cursor.execute("""TRUNCATE Person""")
        cursor.execute("""TRUNCATE Organization""")
        cursor.execute("""TRUNCATE Client""")
        cursor.execute("""TRUNCATE Branch""")
        cursor.execute("""TRUNCATE Log""")
        cursor.execute("""SET FOREIGN_KEY_CHECKS = 1""")
        cursor.execute("""DROP VIEW IF EXISTS Passport""")
        cursor.execute("""DROP VIEW IF EXISTS Passport_clear""")
        db.commit()
    except MySQLdb.Error as error:
        print(error)
    else:
        print("Database truncated")
    db.close()

if __name__ == '__main__':
    main()
