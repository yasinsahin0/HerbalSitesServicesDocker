import pyodbc

class Delete:
    def __init__(self):
        self.db_con = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=sql.athena.domainhizmetleri.com;'
            'Database=<database_name>;'
            'UID=<db_uid>;'
            'PWD=<password>;'
        )
    def cart_delete(self, user_id):
        try:
            curs = self.db_con.cursor()
            curs.execute('DELETE FROM [db_name].[Cart] WHERE UserID = ? ', user_id)
            self.db_con.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def order_detail_delete(self):
        try:
            curs = self.db_con.cursor()
            curs.execute('DELETE FROM [db_name].[OrderDetail]')
            self.db_con.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def order_delete(self):
        try:
            curs = self.db_con.cursor()
            curs.execute('DELETE FROM [db_name].[Order]')
            self.db_con.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

# nesne = Delete()
# nesne.order_detail_delete()
# nesne.order_delete()