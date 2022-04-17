import couchdb
import db_insert as insert

class Query:

    def __init__(self):
        self.db_connection = couchdb.Server("http://admin:admin@172.105.73.62:5984/")

    def user_query(self, mail):
        try:
            database = self.db_connection["users"]
            for doc in database.find({'selector': {"mail": mail}}):

                docx = {
                    "id": doc["_id"],
                    "name": doc["name"],
                    "surname": doc["surname"],
                    "phone_no": doc["phone_no"],
                    "password": doc["password"]
                }
                return docx
        except Exception as e:
            return str(e)

    def product_query(self, name):
        try:
            database = self.db_connection["products"]
            for doc in database.find({'selector': {"name": name.lower()}}):
                docx = {
                    "id": doc["_id"],
                    "name": doc["name"],
                    "content": doc["content"],
                    "price": doc["price"]
                }
                return docx
        except Exception as e:
            return str(e)

    def shop_cart_query(self, user_mail):
        try:
            meta_doc = {}
            count = 0
            database_user = self.db_connection["users"]
            for doc in database_user.find({'selector': {"mail": user_mail}}):
                database_shop = self.db_connection["shop_cart"]
                for doca in database_shop.find({'selector': {"user_id": doc["_id"]}}):
                    count += 1
                    docx = {
                            "product_id": doca["product_id"],
                            "product_name": doca["product_name"],
                            "product_content": doca["product_content"],
                            "product_price": doca["product_price"]
                    }
                    meta_doc.update({count: docx})
            return meta_doc
        except Exception as e:
            return str(e)


    def admin_query(self, mail, password):
        try:
            database = self.db_connection["admin"]
            for doc in database.find({'selector': {"mail": mail}}):
                if password == doc["password"]:
                    return True
            return False
        except Exception as e:
            return str(e)

    def order_shopcart_query(self, user_mail):
        try:
            ins = insert.Insert()
            doc = self.user_query(user_mail)

            database = self.db_connection["shop_cart"]
            for docx in database.find({'selector': {"user_id": doc["id"]}}):
                document = {
                    "user_mail": user_mail,
                    "product_id": docx["product_id"],
                    "product_name": docx["product_name"],
                    "product_content": docx["product_content"],
                    "product_price": docx["product_price"],
                }
                if ins.order_insert(document):
                    database.delete(docx)
            return True

        except Exception as e:
            return str(e)


    def user_control_query(self, mail):
        database = self.db_connection["users"]
        for doc in database.find({'selector': {"mail": mail}}):
            return True
        return False

query = Query()
query.order_shopcart_query("yasin@mail.com")
# if __name__ == "__main__":
#     query = Query()
#     print(query.shop_cart_query("test@gmail.com"))
#     print(query.product_query("Test yeni ürün"))
#     query.user_query("test@gmail.com")
#     print(query.user_control_query("test@gmail.com"))