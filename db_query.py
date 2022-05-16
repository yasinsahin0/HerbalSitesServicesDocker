import pyodbc
import random
import datetime
import db_update as update
import db_insert as insert
import db_delete as delete

class Query:
    def __init__(self):
        self.db_con = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=sql.athena.domainhizmetleri.com;'
            'Database=<database_name>;'
            'UID=<db_uid>;'
            'PWD=<password>;'
        )

    def admin_login_query(self, admin_mail, admin_password):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Admin] WHERE Mail = ? AND Password = ?',
                         admin_mail,
                         admin_password)
            datatable = curs.fetchall()
            for data in datatable:
                return True
            return False
        except Exception as e:
            e = str(e)
            return e

    def user_login_query(self, user_mail, user_password):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[User] WHERE Mail = ? AND Password = ?',
                         user_mail,
                         user_password)
            datatable = curs.fetchall()
            for data in datatable:
                return True
            return False
        except Exception as e:
            e = str(e)
            return e

    def user_query(self, user_mail):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[User] WHERE Mail = ? ', user_mail)
            datatable = curs.fetchall()
            for data in datatable:
                dictionary = {
                    "id": data[0],
                    "Name": data[1],
                    "Surname": data[2],
                    "Mail": data[3],
                    "Phone": data[4],
                    "Password": data[5],
                    "City": data[6],
                    "District": data[7],
                    "Adress": data[8],
                    "Status": data[9]
                }
                return dictionary
            return "False"
        except Exception as e:
            e = str(e)
            return e

    def cart_query(self, user_id):
        try:
            dicx ={}
            count = 0
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Cart] WHERE UserID = ? ', user_id)
            datatable = curs.fetchall()
            for data in datatable:
                count += 1
                dictionary = {
                    "id": data[0],
                    "UserID": data[1],
                    "ProductID": self.product_query(data[2]),
                    "Count": data[3]
                }
                dicx.update({count: dictionary})

            return dicx
        except Exception as e:
            e = str(e)
            return e

    def product_query(self, product_id):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Product] WHERE ID = ? ', int(product_id))
            datatable = curs.fetchall()
            for data in datatable:
                dictionary = {
                    "ProductID": data[0],
                    "Name": data[1],
                    "Price": data[2],
                    "Content": data[3],
                    "Stok": data[4],
                    "Category": data[5]
                }
                return dictionary
            return "False"
        except Exception as e:
            e = str(e)
            return e

    def product_last_five_query(self):
        try:
            dict_meta = {}
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Product]')
            datatable = curs.fetchall()
            counter = 0
            for i in range(len(datatable), 0, -1):
                counter += 1
                dictionary = self.product_query(i)
                dict_meta.update({counter: dictionary})
                if counter == 5:
                    return dict_meta

            return "False"
        except Exception as e:
            e = str(e)
            return e

    def top_sellers_query(self, count):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[OrderDetail] ORDER BY Count DESC')
            datatable = curs.fetchall()
            dicte = {}
            counter = 0
            for data in datatable:
                counter += 1
                product_dict = self.product_query(data[1])
                dicte.update({counter: product_dict})

                if count == counter:
                    return dicte
        except Exception as e:
            e = str(e)
            return e

    def image_query(self, product_id):
        try:
            dict_meta = {}
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[İmage] WHERE ProductID = ?', int(product_id))
            datatable = curs.fetchall()
            counter = 0
            for data in datatable:
                counter += 1
                dicte = {
                    "ProductID": data[1],
                    "URL": data[2],
                }
                dict_meta.update({counter: dicte})

            return dict_meta
        except Exception as e:
            e = str(e)
            return e

    def product_price_query(self, product_id, product_count):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Product] WHERE ID = ?', int(product_id))
            datatable = curs.fetchall()
            for data in datatable:
               return data[2] * product_count
        except Exception as e:
            e = str(e)
            return e

    def random_product_query(self, count):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Product]')
            datatable = curs.fetchall()
            dicte = {}
            counter = 0
            for i in range(0,count):
                counter += 1
                rndm = random.randint(1, len(datatable))
                curs = self.db_con.cursor()
                curs.execute('SELECT * FROM [db_name].[Product] WHERE ID = ?', rndm)
                dtable = curs.fetchall()
                for data in dtable:
                    dicx = {
                        "ProductID": data[0],
                        "Name": data[1],
                        "Price": data[2],
                        "Content": data[3],
                        "Stok": data[4],
                        "Category": data[5]
                    }
                    dicte.update({counter: dicx})
                if count == counter:
                    return dicte
            return "False"
        except Exception as e:
            e = str(e)
            return e

    def product_list_query(self, page_number):
        try:
            dicte = {}
            curs = self.db_con.cursor()
            curs.execute('SELECT TOP 12 * FROM [db_name].[Product] WHERE ID <= ? AND ID > ? ORDER BY ID DESC', page_number*12, page_number*12-12)
            datatable = curs.fetchall()
            counter = 0
            for data in datatable:
                counter += 1
                dicx = {
                    "ProductID": data[0],
                    "Name": data[1],
                    "Price": data[2],
                    "Content": data[3],
                    "Stok": data[4],
                    "Category": data[5]
                }
                dicte.update({counter: dicx})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def cart_price_count_query(self, user_id):
        try:

            curs = self.db_con.cursor()
            curs.execute('SELECT ProductID,Count FROM [db_name].[Cart] WHERE UserID = ?', user_id)
            datatable = curs.fetchall()
            product_count = 0
            cart_price = 0
            for data in datatable:
                curs = self.db_con.cursor()
                curs.execute('SELECT Price FROM [db_name].[Product] WHERE ID = ?', data[0])
                datat = curs.fetchall()

                for dt in datat:
                    product_count += data[1]
                    cart_price += dt[0]*data[1]
            dicte = {"total_product":product_count,
                     "total_price":cart_price}
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def total_product_page_count(self):
        try:
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Product]')
            datatable = curs.fetchall()
            counter = 0
            for data in datatable:
                counter += 1
            page_count = int(counter / 12) + 1
            dicte = {"product_count": counter,
                     "page_count": page_count}
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def order_query(self, user_id):
        try:

            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Order] WHERE UserID = ? ', int(user_id))
            datatable = curs.fetchall()

            for data in datatable:

                dictionary = {
                    "id": data[0],
                    "UserID": data[1],
                    "Status": data[2],
                    "InsertDate": data[3],
                    "UpdateDate": data[4]
                }

                return dictionary

        except Exception as e:
            e = str(e)
            return e

    def orders_query(self, user_id):
        try:
            dicte = {}
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Order] WHERE UserID = ? ', int(user_id))
            datatable = curs.fetchall()
            counter = 0
            for data in datatable:
                counter += 1
                dictionary = {
                    "id": data[0],
                    "UserID": data[1],
                    "Status": data[2],
                    "InsertDate": data[3],
                    "UpdateDate": data[4]
                }
                dicte.update({counter: dictionary})
            return dicte

        except Exception as e:
            e = str(e)
            return e

    def cart_local_query(self, user_id):
        try:
            counter = 0
            dicte = {}
            curs = self.db_con.cursor()
            curs.execute('SELECT * FROM [db_name].[Cart] WHERE UserID = ? ', int(user_id))
            datatable = curs.fetchall()
            for data in datatable:
                counter += 1
                dictionary = {
                    "ProductID": data[2],
                    "Count": data[3]
                }
                dicte.update({counter: dictionary})
            return dicte

        except Exception as e:
            e = str(e)
            return e

    def order_insert_que(self, user_id, status):
        try:
            insert_date = datetime.datetime.now()
            update_date = datetime.datetime.now()
            curs = self.db_con.cursor()
            curs.execute("INSERT INTO [db_name].[Order] (UserID,Status,InsertDate,UpdateDate) VALUES (?,?,?,?)",
                            int(user_id),
                            int(status),
                            insert_date,
                            update_date)
            curs.commit()
            return True
        except Exception as e:
            e = str(e)
            return e

    def cart_user_id_insert(self, user_id):
        try:
            order_insert_return = self.order_insert_que(user_id, 0)
            if order_insert_return:
                order_query_return = self.order_query(user_id)
                if order_query_return != False:
                    order_id = order_query_return["id"]
                    cart_query_return = self.cart_local_query(user_id)
                    order_detail = False
                    for i in range(1, len(cart_query_return)+1):
                        product_id = cart_query_return[i]["ProductID"]
                        product_count = cart_query_return[i]["Count"]
                        upd = update.Update()
                        upd.product_stock_decrease(product_id,product_count)
                        product_que_return = self.product_query(product_id)
                        product_price = product_que_return["Price"]
                        ins = insert.Insert()
                        order_detail = ins.order_detail_insert(product_id, product_price, product_count, order_id)
                    dele = delete.Delete()
                    if order_detail:
                        dele.cart_delete(user_id)
                        return True
        except Exception as e:
            return str(e)



# nesne = Query()
# print(nesne.cart_user_id_insert(1))
# print(nesne.cart_local_query(2))
# print(nesne.total_product_page_count())