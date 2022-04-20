import pyodbc
import datetime


class Insert:
    def __init__(self):
        self.db_con = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=sql.athena.domainhizmetleri.com;'
            'Database=abdullah_web;'
            'UID=abdullah_pys;'
            'PWD=@PassWord123;'
        )

    def test(self):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[İmage]')
            users = curs.fetchall()
            for i in users:
                print(i)
        except Exception as e:
            print(e)

    def status_insert(self, name, status_id):
        try:
            curs = self.db_con.cursor()
            curs.execute(
                "insert into Status(ID,Name) values (?, ?)", status_id, str(name))
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def user_insert(self, user_name, user_surname, user_mail, user_phone, user_pass, user_city, user_district, user_adress, user_status):
        try:

            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [abdullah_pys].[User] (Name,Surname,Mail,Phone,Password,City,District,Adress,Status) VALUES (?,?,?,?,?,?,?,?,?)",
                            str(user_name),
                            str(user_surname),
                            str(user_mail),
                            str(user_phone),
                            str(user_pass),
                            str(user_city),
                            str(user_district),
                            str(user_adress),
                            int(user_status))
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def product_insert(self, product_name, product_price, product_content, product_stock, product_category):
        try:

            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [abdullah_pys].[Product] (Name,Price,[Content],Stok,Category) VALUES (?,?,?,?,?)",
                            str(product_name),
                            product_price,
                            str(product_content),
                            int(product_stock),
                            str(product_category))
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def product_image_insert(self, product_id, product_image_url):
        try:
            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [abdullah_pys].[İmage] (ProductID,URL) VALUES (?,?)",
                            int(product_id),
                            product_image_url)
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def cart_insert(self, user_id, product_id, count):
        try:

            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [abdullah_pys].[Cart] (UserID,ProductID,Count) VALUES (?,?,?)",
                            int(user_id),
                            int(product_id),
                            int(count))
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def order_insert(self, user_id, status):
        try:
            insert_date = datetime.datetime.now()
            update_date = datetime.datetime.now()
            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [abdullah_pys].[Order] (UserID,Status,InsertDate,UpdateDate) VALUES (?,?,?,?)",
                            int(user_id),
                            int(status),
                            insert_date,
                            update_date)
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def order_detail_insert(self, product_id, product_price, count, order_id):
        try:
            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [abdullah_pys].[OrderDetail] (ProductID,ProductPrice,Count,OrderID) VALUES (?,?,?,?)",
                            int(product_id),
                            product_price,
                            int(count),
                            int(order_id))
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

