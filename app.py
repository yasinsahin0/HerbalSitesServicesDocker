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

@app.route('/status_insert', methods=['POST'])
def status_insert():
    print('[INFO]--[test]--[FUNCTION]')
    name = request.form['name']
    status_id = request.form['status_id']
    ins = insert.Insert()
    result = ins.status_insert(name, status_id)
    return str(result)

@app.route('/user_insert', methods=['POST'])
def user_insert():
    print('[INFO]--[test]--[FUNCTION]')
    user_name = request.form['user_name']
    user_surname = request.form['user_surname']
    user_mail = request.form['user_mail']
    user_phone = request.form['user_phone']
    user_pass = request.form['user_pass']
    user_city = request.form['user_city']
    user_district = request.form['user_district']
    user_adress = request.form['user_adress']
    user_status = request.form['user_status']
    ins = insert.Insert()
    result = ins.user_insert(user_name, user_surname, user_mail, user_phone, user_pass, user_city, user_district, user_adress, user_status)
    return str(result)

@app.route('/product_insert', methods=['POST'])
def product_insert():
    print('[INFO]--[test]--[FUNCTION]')
    product_name = request.form['product_name']
    product_price = request.form['product_price']
    product_content = request.form['product_content']
    product_stock = request.form['product_stock']
    product_category = request.form['product_category']
    ins = insert.Insert()
    result = ins.product_insert(product_name, product_price, product_content, product_stock, product_category)
    return str(result)

@app.route('/product_image_insert', methods=['POST'])
def product_image_insert():
    print('[INFO]--[test]--[FUNCTION]')
    product_id = request.form['product_id']
    product_image_url = request.form['product_image_url']
    ins = insert.Insert()
    result = ins.product_image_insert(product_id, product_image_url)
    return str(result)

@app.route('/cart_insert', methods=['POST'])
def cart_insert():
    print('[INFO]--[test]--[FUNCTION]')
    user_id = request.form['user_id']
    product_id = request.form['product_id']
    count = request.form['count']
    ins = insert.Insert()
    result = ins.cart_insert(user_id, product_id, count)
    return str(result)

@app.route('/order_insert', methods=['POST'])
def order_insert():
    print('[INFO]--[test]--[FUNCTION]')
    user_id = request.form['user_id']
    status = request.form['status']
    ins = insert.Insert()
    result = ins.order_insert(user_id, status)
    return str(result)

@app.route('/order_detail_insert', methods=['POST'])
def order_detail_insert():
    print('[INFO]--[test]--[FUNCTION]')
    product_id = request.form['product_id']
    product_count = request.form['product_count']
    order_id = request.form['order_id']
    ins = insert.Insert()
    result = ins.order_detail_insert(product_id, product_count, order_id)
    return str(result)

@app.route('/admin_login_query', methods=['POST'])
def admin_login_query():
    print('[INFO]--[test]--[FUNCTION]')
    admin_mail = request.form['admin_mail']
    admin_password = request.form['admin_password']
    que = query.Query()
    result = que.admin_login_query(admin_mail, admin_password)
    return str(result)

@app.route('/user_login_query', methods=['POST'])
def user_login_query():
    print('[INFO]--[test]--[FUNCTION]')
    user_mail = request.form['user_mail']
    user_password = request.form['user_password']
    que = query.Query()
    result = que.user_login_query(user_mail, user_password)
    return str(result)

@app.route('/user_query', methods=['POST'])
def user_query():
    print('[INFO]--[test]--[FUNCTION]')
    user_mail = request.form['user_mail']
    que = query.Query()
    result = que.user_query(user_mail)
    return result

@app.route('/cart_query', methods=['POST'])
def cart_query():
    print('[INFO]--[test]--[FUNCTION]')
    user_id = request.form['user_id']
    que = query.Query()
    result = que.cart_query(user_id)
    return result

@app.route('/product_query', methods=['POST'])
def product_query():
    print('[INFO]--[test]--[FUNCTION]')
    product_id = request.form['product_id']
    que = query.Query()
    result = que.product_query(product_id)
    return result

@app.route('/product_last_five_query', methods=['POST'])
def product_last_five_query():
    print('[INFO]--[test]--[FUNCTION]')
    que = query.Query()
    result = que.product_last_five_query()
    return result

@app.route('/top_sellers_query', methods=['POST'])
def top_sellers_query():
    print('[INFO]--[test]--[FUNCTION]')
    count = request.form['count']
    que = query.Query()
    result = que.top_sellers_query(int(count))
    return result

@app.route('/image_query', methods=['POST'])
def image_query():
    print('[INFO]--[test]--[FUNCTION]')
    product_id = request.form['product_id']
    que = query.Query()
    result = que.image_query(product_id)
    return result

@app.route('/product_price_query', methods=['POST'])
def product_price_query():
    print('[INFO]--[test]--[FUNCTION]')
    product_id = request.form['product_id']
    product_count = request.form['product_count']
    que = query.Query()
    result = que.product_price_query(int(product_id),float(product_count))
    return str(result)

@app.route('/product_list_query', methods=['POST'])
def product_list_query():
    print('[INFO]--[test]--[FUNCTION]')
    page_number = request.form['page_number']
    que = query.Query()
    result = que.product_list_query(int(page_number))
    return result

@app.route('/random_product_query', methods=['POST'])
def random_product_query():
    print('[INFO]--[test]--[FUNCTION]')
    count = request.form['count']
    que = query.Query()
    result = que.random_product_query(int(count))
    return result

if __name__ == '__main__':
    app.run()