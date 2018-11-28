# __author__ = 'Administrator'
import MySQLdb


class Db:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self._conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db, charset='utf8')
        self._cursor = self._conn.cursor()

    def fetchone(self, sql):
        self._cursor.execute(sql)
        result = self._cursor.fetchone()
        return result


h = '127.0.0.1'
u = 'root'
p = 'redhat'
database = 'mysql'
sql_example = "select user from user where user='root'"
d = Db(h, u, p, database)
res = d.fetchone(sql_example)
print(res[0])
