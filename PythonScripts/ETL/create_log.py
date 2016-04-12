import MySQLdb


def create_table(db):
    try:
        cur = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Log(
            log_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            req_type VARCHAR(30) NOT NULL,
            log_table VARCHAR(30) NOT NULL,
            c_id INT NOT NULL,
            time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )"""
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
        create_table(db)
