import couchdb

class Delete:

    def __init__(self):
        self.db_connection = couchdb.Server("http://admin:admin@172.105.73.62:5984/")

    def shop_cart_delete(self, user_mail, product_name):
        try:
            dx = None
            database_user = self.db_connection["users"]
            for doc in database_user.find({'selector': {"mail": user_mail}}):
                database_shop = self.db_connection["shop_cart"]
                for docx in database_shop.find({'selector': {"user_id": doc["_id"]}}):
                    for d in database_shop.find({'selector': {"product_name": product_name}}):
                        dx = d
            database_shops = self.db_connection["shop_cart"]
            database_shops.delete(dx)
            return True
        except Exception as e:
            return str(e)


# dele = Delete()
# dele.shop_cart_delete("test@gmail.com", "test 1")