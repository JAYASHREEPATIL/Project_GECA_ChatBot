import mysql.connector


def insert_data(uname, passwd):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    sql = 'INSERT INTO login(username, password) VALUES ("{0}","{1}");'.format(uname, passwd)
    dbcursor.execute(sql)
    mysqldb.commit()


def fetch_data():
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    dbcursor.execute("select * from login")
    result=dbcursor.fetchall()
    return result


def fetch_details(uname):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    sql='select * from studentdetails where Roll_no=("{0}")'.format(uname)
    dbcursor.execute(sql)
    result=dbcursor.fetchall()
    return result

def get_sem(uname):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    sql = 'select semester from studentdetails where Roll_no = ("{0}")'.format(uname)
    dbcursor.execute(sql)
    result=dbcursor.fetchone()
    return result

def addoptcourse(uname,optcourse):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    sql = 'INSERT INTO optional_course(uname,optcourse) VALUES ("{0}","{1}");'.format(uname,optcourse)
    dbcursor.execute(sql)
    mysqldb.commit()