from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)

connection = psycopg2.connect(
    host='localhost',
    dbname='todo',
    user='postgres',
    password='password',
)

@app.route('/todo-lists', methods=['GET'])
def get_todo_lists():
    sql = '''
    SELECT * FROM rogin;
    '''
    result = connection.execute(sql)
    todo_lists = []
    for row in result:
        todo_list = {
            'ID': row[0],
            'RoginID' :row[1],
            'password': row[2]
        }
        todo_lists.append(todo_list)
    return jsonify(todo_lists)


@app.route('/todo-lists', methods=['POST'])
def post_todo_list():

    sql = '''
    SELECT ID
    FROM rogin;
    '''
    result = connection.execute(sql)
    key = []
    for row in result:
        key.append(row[0])
    new_key = 1
    while True:
        if new_key not in key:
            break
        new_key += 1
    content = request.get_json()

    try:
        sql = '''
        INSERT INTO rogin (ID, RoginID, password)
        VALUES
        (%(ID)s, %(RoginID)s, %(Password)s);
        '''

        connection.execute(sql, {'ID': new_key, 'RoginID': content["RoginID"], 'Password': content["password"]})

    except Exception:
        connection.rollback()
    else:
        connection.commit()

    return jsonify({'message': 'created'})
