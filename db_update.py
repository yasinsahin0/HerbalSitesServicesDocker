import pyodbc

class Update:
    def __init__(self):
        self.db_con = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=sql.athena.domainhizmetleri.com;'
            'Database=abdullah_web;'
            'UID=abdullah_pys;'
            'PWD=@PassWord123;'
        )

    def product_stock_decrease(self, product_id, decrease_count):
        cursor = self.db_con.cursor()
        cursor.execute("UPDATE Product SET Stok = ? WHERE ID = ?", int(decrease_count), int(product_id))
        self.db_con.commit()
        return "Successful"