from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Anirudh005:Ani@Anirudh005.mysql.pythonanywhere-services.com:3306/Anirudh005$Content'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('content', db.String(255))

@app.route('/')
def root():
    try:
        tasks = Task.query.all()  # Query all tasks
        return render_template("base.html", tasks=tasks)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/home", methods=['POST'])
def add():
    try:
        task_content = request.form['content']
        if not task_content:
            return redirect(url_for('root'))

        new_task = Task(title=task_content,)  # Adjust this based on your needs
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('root'))
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        return redirect(url_for('root'))
    except Exception as e:
        return redirect(url_for('root'))

@app.route("/home1", methods=['POST'])
def remove():
    task_content = request.form['content1']
    try:
        task_to_delete = Task.query.filter_by(title=task_content).first()
        if task_to_delete:
            db.session.delete(task_to_delete)
            db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()

    return redirect(url_for('root'))
@app.route('/re')
def nxt1():
   return render_template("re.html")

@app.route ('/index_add')
def nxt():
   return render_template("index_add.html")



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
