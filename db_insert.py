import couchdb

class Insert():

    def __init__(self):
        self.db_connection = couchdb.Server("http://admin:admin@172.105.73.62:5984/")

    def product_insert(self, pro_id, name, content, price):
        database = self.db_connection["products"]
        doc = {"pro_id":pro_id,
               "name":name,
               "content":content,
               "price":price}
        database.save(doc)

    def test(self):
        database = self.db_connection["products"]
        for d in database:
            for doc in database.find({'selector': {"_id": d}}):
                print(doc)
                print(type(doc))


if __name__ == "__main__":
    insert = Insert()
    # insert.product_insert(111,"test","test cont",41.21)