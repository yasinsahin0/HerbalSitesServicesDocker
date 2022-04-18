import pyodbc

class Test:
    def __init__(self):
        self.db_con = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=sql.athena.domainhizmetleri.com;'
            'Database=abdullah_web;'
            'UID=abdullah_pys;'
            'PWD=@PassWord123;'
        )
    def admin(self):
        print("\n")
        print("Admin Tablosu - ID, Name, Surname, Mail, Password")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[Admin]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def user(self):
        print("\n")
        print("User Tablosu - ID, Name, Surname, Mail, Phone, Password, City, District, Adress, Status")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[User]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def product(self):
        print("\n")
        print("Product Tablosu - ID, Name, Price, Content, Stok, Category")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[Product]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def image(self):
        print("\n")
        print("İmage Tablosu - ID, ProductID, URL")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[İmage]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def cart(self):
        print("\n")
        print("Cart Tablosu - ID, UserID, ProductID, Count")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[Cart]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def order(self):
        print("\n")
        print("Order Tablosu - ID, UserID, Status, İnsertDate, UpdateDate")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[Order]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def order_detail(self):
        print("\n")
        print("OrderDetail Tablosu - ProductID, ProductPrice, Count, OrderID")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[OrderDetail]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def status(self):
        print("\n")
        print("Status Tablosu - ID, Name")
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[Status]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)



if __name__ == "__main__":
    tst = Test()
    tst.admin()
    tst.user()
    tst.product()
    tst.cart()
    tst.order()
    tst.order_detail()
    tst.status()