from flask import Flask, request, jsonify
import psycopg2
import sqlalchemy
# from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
import env

app = Flask(__name__)

# open cors
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/', methods=['get'])
def get():
    # db connection
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    con = psycopg2.connect(
        host = 'localhost',
        database = 'postgres',
        user = USERNAME,
        password = PASSWORD
    )
    
    # create db cursor
    cur = con.cursor()
    # query
    data = []

    # testing purposes
    # cur.execute("INSERT INTO shrooms (temperature, humidity, co2) VALUES (%s, %s, %s)", (79.2, 82.1, 891.7))

    cur.execute('SELECT temperature, humidity, co2 FROM shrooms')
    rows = cur.fetchall()
    for r in rows:
        data.append({'temperature': r[0], 'humidity': r[1], 'co2': r[2]})

    # close cursor
    cur.close()

    #close connection
    con.close()    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)