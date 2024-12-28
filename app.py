from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rahma@131.Com'
app.config['MYSQL_DB'] = 'tour_agency_db'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM messages")
    data = cur.fetchall()
    cur.close()
    
    return str(data)

if __name__ == '_main_':
    app.run(debug=True)