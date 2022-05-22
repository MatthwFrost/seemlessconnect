from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

# Function to add data to the db
def add_data(content):
    cur.execute(f"INSERT INTO data (CONTENT) VALUES ('{content}')")
    conn.commit()

# Fetches all data in the "Data" table
def fetch_all():
    all_data = cur.execute(f"SELECT * FROM data;").fetchall()
    return all_data

# Home route
@app.route('/', methods=['GET'])
def home():
    return "<p>blah</p>"

@app.route('/fetch/', methods=['GET'])
def fetch():
    #conn = sqlite3.connect('scdatabase.db', check_same_thread=False)
    #cur = conn.cursor()
    all_data = fetch_all()
    #all_data = cur.execute('SELECT * FROM data;').fetchall()
    return jsonify(all_data)

# *** Add data to db ***
# 127.0.0.01/post?content=* 
@app.route('/post/', methods=['GET'])
def post():
    query_parameters = request.args
    content = query_parameters.get('content')
    add_data(content)
    return f"<p> Adding {content} to the database"

if __name__ == '__main__':
    path = '../database/data.db'
    conn = sqlite3.connect(path, check_same_thread=False)
    cur = conn.cursor()

    app.run(host="192.168.128.241")

