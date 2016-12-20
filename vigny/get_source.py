class GetSource(object):
    def get_source(self, category):
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="newssource", charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT "