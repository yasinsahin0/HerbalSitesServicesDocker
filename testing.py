import couchdb

class Testing:
    def __init__(self):
        self.db_connection = couchdb.Server("http://admin:admin@172.105.73.62:5984/")


    def database_test(self):
        for dbname in self.db_connection:
            print("Database name : ",dbname)

    def products_test(self):
        count = 0
        database = self.db_connection["products"]
        for docid in database.view('_all_docs'):
            count += 1
            doc = docid["id"]
            a = database[doc]
            print("Products "+str(count)+ " : ",a["pro_id"], a["name"],a["content"],a["price"])

if __name__ == "__main__":
    test = Testing()
    test.database_test()
    test.products_test()