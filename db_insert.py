import couchdb
import db_query as que

class Insert:

    def __init__(self):
        self.db_connection = couchdb.Server("http://admin:admin@172.105.73.62:5984/")

    def product_insert(self, name, content, price):
        try:
            if self.db_name_query("products"):
                database = self.db_connection["products"]
                doc = {"name": name.lower(),
                       "content": content,
                       "price": price}
                database.save(doc)
                return True
            else:
                return False
        except Exception as e:
            return str(e)

    def order_insert(self, document):
        try:
            if self.db_name_query("orders"):
                database = self.db_connection["orders"]
                database.save(document)
                return True
            else:
                return False
        except Exception as e:
            return str(e)

    def user_insert(self, name, surname, mail, phone_no, password):
        try:
            query = que.Query()
            if phone_no[0:2] == "+9":
                phone_no = phone_no[2:]
            if phone_no[0] == "9":
                phone_no = phone_no[1:]

            if query.user_control_query(mail):
                return False
            else:
                if self.db_name_query("users"):
                    database = self.db_connection["users"]
                    doc = {"name": name,
                           "surname": surname,
                           "mail": mail,
                           "phone_no": int(phone_no),
                           "password": password}
                    database.save(doc)
                    return True
                else:
                    return False
        except Exception as e:
            return str(e)

    def shop_cart_insert(self, user_mail, pro_name):
        try:
            query = que.Query()
            user_doc = query.user_query(user_mail)
            products_doc = query.product_query(pro_name)
            if self.db_name_query("shop_cart"):
                database = self.db_connection["shop_cart"]
                doc = {
                    "user_id": user_doc["id"],
                    "product_id": products_doc["id"],
                    "product_name": products_doc["name"],
                    "product_content": products_doc["content"],
                    "product_price": products_doc["price"]
                }
                database.save(doc)
                return True
            else:
                return False
        except Exception as e:
            return str(e)

    def admin_insert(self, admin_mail, admin_password):
        try:
            if self.db_name_query("admin"):
                database = self.db_connection["admin"]
                doc = {"mail": admin_mail,
                       "password": admin_password}
                database.save(doc)
                return True
            else:
                return False
        except Exception as e:
            return str(e)

    def db_name_query(self, dbname):
        for i in self.db_connection:
            if i == dbname:
                return True
        self.db_connection.create(dbname)
        return True




# if __name__ == "__main__":
#     insert = Insert()
#     print(insert.admin_insert("admin", "test123"))
#     print(insert.user_insert("test1","test1","test1@gmail.com","+905415552266","test123"))
#     print(insert.product_insert("Test 3", "test cont", 99.21))
#     print(insert.shop_cart_insert("test@gmail.com","test 2"))
