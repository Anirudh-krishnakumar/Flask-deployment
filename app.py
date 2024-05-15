from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ani@2004'
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task_content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (content) VALUES (%s)", (task_content,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('info_view'))

@app.route('/info_view')
def info_view():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
        cur.close()
        return render_template("index1.html", remain=tasks)
    except Exception as e:
        error_message = str(e)
        return render_template("error.html", error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)