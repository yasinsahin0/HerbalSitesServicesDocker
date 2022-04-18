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


if __name__ == '__main__':
    app.run()