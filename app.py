from flask import Flask, request
import db_insert as insert
import db_query as query
import db_delete as delete


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/test', methods=['POST'])
def test():
    print('[INFO]--[test]--[FUNCTION]')
    return "Test Başarılı"


@app.route('/ProductInsert', methods=['POST'])
def ProductInsert():
    try:
        ins = insert.Insert()
        name = request.form["name"]
        content = request.form["content"]
        price = request.form["price"]
        result = ins.product_insert(name, content, price)
        if result:
            return str(result)
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/UserInsert', methods=['POST'])
def UserInsert():
    try:
        ins = insert.Insert()
        name = request.form["name"]
        surname = request.form["surname"]
        mail = request.form["mail"]
        phone_no = request.form["phone_no"]
        password = request.form["password"]
        result = ins.user_insert(name, surname, mail, phone_no, password)
        if result:
            return str(result)
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/ShopCartInsert', methods=['POST'])
def ShopCartInsert():
    try:
        ins = insert.Insert()
        user_mail = request.form["user_mail"]
        product_name = request.form["product_name"]
        result = ins.shop_cart_insert(user_mail, product_name)
        if result:
            return str(result)
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/AdminInsert', methods=['POST'])
def AdminInsert():
    try:
        ins = insert.Insert()
        admin_mail = request.form["admin_mail"]
        admin_password = request.form["admin_password"]
        result = ins.admin_insert(admin_mail, admin_password)
        if result:
            return str(result)
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"


@app.route('/UserQuery', methods=['POST'])
def UserQuery():
    try:
        que = query.Query()
        user_mail = request.form["user_mail"]
        result = que.user_query(user_mail)
        if result:
            return result
        elif result == None:
            return "False"
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/ProductQuery', methods=['POST'])
def ProductQuery():
    try:
        que = query.Query()
        product_name = request.form["product_name"]
        result = que.product_query(product_name)
        if result:
            return result

        elif result == None:
            return "False"
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/ShopCartQuery', methods=['POST'])
def ShopCartQuery():
    try:
        que = query.Query()
        user_mail = request.form["user_mail"]
        result = que.shop_cart_query(user_mail)
        if result:
            return result

        elif result == None:
            return "False"
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/AdminQuery', methods=['POST'])
def AdminQuery():
    try:
        que = query.Query()
        admin_mail = request.form["admin_mail"]
        admin_password = request.form["admin_password"]
        result = que.admin_query(admin_mail, admin_password)
        if result:
            return str(result)

        elif result == None:
            return "False"
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

@app.route('/ShopCartDelete', methods=['POST'])
def ShopCartDelete():
    try:
        delet = delete.Delete()
        user_mail = request.form["user_mail"]
        product_name = request.form["product_name"]
        result = delet.shop_cart_delete(user_mail, product_name)
        if result:
            return str(result)

        elif result == None:
            return "False"
        else:
            return str(result)
    except KeyError as e:
        return "Key Error"

if __name__ == '__main__':
    app.run()