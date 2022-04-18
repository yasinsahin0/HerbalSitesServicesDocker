import pyodbc

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
            curs.execute('SELECT * FROM [abdullah_pys].[User]')
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
            return "Successful"
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
            return "Successful"
        except Exception as e:
            e = str(e)
            return e



nesne = Insert()
nesne.test()

#print(nesne.user_insert("Yasin","Şahin","yasin@mail.com","0541884423","test123","Samsun","Hançerli mahallesi","Test adres",2))

# nesne.admin_insert("test","test","test@mail.com","test123")
# nesne.test()