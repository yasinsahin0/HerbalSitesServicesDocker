import pyodbc

class Delete:
    def __init__(self):
        self.db_con = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=sql.athena.domainhizmetleri.com;'
            'Database=abdullah_web;'
            'UID=abdullah_pys;'
            'PWD=@PassWord123;'
        )
    def cart_delete(self, user_id):
        try:
            curs = self.db_con.cursor()
            curs.execute('DELETE FROM [abdullah_pys].[Cart] WHERE UserID = ? ', user_id)
            self.db_con.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

