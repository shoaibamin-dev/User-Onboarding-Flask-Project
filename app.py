from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from base64 import b64encode
import base64
from io import BytesIO

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bank_employee_mgt'

mysql = MySQL(app)


def queryTable():
    with app.app_context():

        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT date from 1046_exam where level = %s''',
                       ("moderate"))
        result = cursor.fetchall()

        cursor.close()

        return result


def all():
    user_data = []
    with app.app_context():

        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * from user ''')
        results = cursor.fetchall()

        for result in results:
            user_data.append([result[0], result[1], result[2],
                              result[3], result[4], result[5], result[6]])

        cursor.close()

        # print(user_data)
        return user_data


def search(user_name, password):
    with app.app_context():

        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * from user where user_name = %s and password = %s''',
                       (user_name, password))
        result = cursor.fetchall()

        cursor.close()

        return result


def save(first_name, last_name, user_name, email, password, icon_data):

    with app.app_context():

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO user (`first_name`, `last_name`, `user_name`, `email`, `password`,`icon`) VALUES( %s,%s, %s, %s, %s, %s)''',
                       (first_name, last_name, user_name, email, password, icon_data))
        mysql.connection.commit()
        cursor.close()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():

    error_msg = ""

    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        user_name = request.form['uname']
        email = request.form['email']
        password = request.form['pass']

        file = request.files['uicon']
        data = file.read()
        icon_data = base64.b64encode(data).decode('ascii')

        save(first_name, last_name, user_name, email, password, icon_data)
        return render_template('login.html', success=True)


@app.route('/login', methods=['POST', 'GET'])
def loginform():

    error_msg = ""

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        user_name = request.form['uname']
        password = request.form['pass']

        print(user_name, password, "USER")

        if(len(search(user_name, password)) > 0):
            all_data = all()
            return render_template('users.html', data=all_data)

        return "User Not Found"


if __name__ == "__main__":
    app.run(debug=True)
