import MySQLdb


def create_tables(db):
    try:
        cur = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Branch(
            branch_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            branch_city VARCHAR(20) NOT NULL,
            branch_address VARCHAR(50) NOT NULL,
            INDEX Index_Branch (branch_id)
            )"""
        cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Client(
            client_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            registration_date DATE NOT NULL,
            INDEX Index_Client (client_id))"""
        cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Person(
            person_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            person_name VARCHAR(50) NOT NULL,
            person_birthday DATE NOT NULL,
            person_gender VARCHAR(10) NOT NULL,
            person_address VARCHAR(100) NOT NULL,
            person_passport VARCHAR(11) NOT NULL,
            client_id INT NOT NULL,
            FOREIGN KEY `p_client_id`(client_id) REFERENCES Client(client_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            INDEX Index_Person (person_id),
            INDEX Index_PClient (client_id))"""
        cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Organization(
            org_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            org_name VARCHAR(50) NOT NULL,
            org_ogrn VARCHAR(13) NOT NULL,
            org_inn VARCHAR(10) NOT NULL,
            foundation_date DATE NOT NULL,
            client_id INT NOT NULL,
            FOREIGN KEY `o_client_id`(client_id) REFERENCES Client(client_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            INDEX Index_Org (org_id),
            INDEX Index_OClient (client_id))"""
        cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Account(
            account_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            balance FLOAT NOT NULL,
            rate FLOAT NOT NULL,
            account_type VARCHAR(10),
            status VARCHAR(10),
            client_id INT NOT NULL,
            branch_id INT NOT NULL,
            FOREIGN KEY `a_client_id`(client_id) REFERENCES Client(client_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY `a_branch_id`(branch_id) REFERENCES Branch(branch_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            INDEX Index_Account (account_id),
            INDEX Index_ABranch (branch_id),
            INDEX Index_AClient (client_id))"""
        cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Loan(
            loan_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            loan_name VARCHAR(20) NOT NULL,
            open_date DATE NOT NULL,
            close_date DATE NULL,
            loan_period INT NOT NULL,
            loan_rest FLOAT NOT NULL,
            loan_rate FLOAT NOT NULL,
            client_id INT NOT NULL,
            FOREIGN KEY `l_client_id`(client_id) REFERENCES Client(client_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            INDEX Index_Loan (loan_id),
            INDEX Index_LClient (client_id))"""
        cur.execute(sql)

        sql = """create table if not exists Payments(
        payment_id int not null auto_increment primary key,
        payment_type varchar(25) not null,
        payment_value int not null,
        payment_date date not null,
        client_id int not null,
        account_id int null;
        loan_id int null;
        foreign key `payment_client_id`(client_id) references Client(client_id)
        on update cascade on delete cascade,
        foreign key `payment_account_id`(account_id) references Account(account_id)
        on update cascade on delete cascade,
        foreign key `payment_loan_id`(loan_id) references Loan(loan_id)
        on update cascade on delete cascade,
        index Index_payment (payment_id),
        index Index_PayClient (client_id),
        index Index_PayAcc (account_id),
        index Index_PayLoan (loan_id))"""
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
        create_tables(db)


# Virtual tables (views)
# create view Passport(id,pass, col) as select person_id, person_passport, count(*) from Person group by(person_passport);
# create view Passport_clear(id_c,pass_c, col_c) as select id, pass, col from Passport where col>1;
# На выходе Passport_clear получаем дублированные паспорта, удаляем этих
# клиентов
