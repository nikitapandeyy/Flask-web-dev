#creating A Minimal Application
from flask import Flask, render_template,request ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
      title=request.form["title"]
      desc=request.form["desc"]
      todo=Todo(title=title,desc=desc)
      db.session.add(todo)
      db.session.commit()
    allTodo=Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)
#connecting with database

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:////tmp/todoo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
db=SQLAlchemy(app)

class Todo(db.Model):
  sno=db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(200),nullable=False)
  desc=db.Column(db.String(500),nullable=True)
  date_create=db.Column(db.DateTime,default=datetime.utcnow)
  
  def __repr__(self) -> str:
    return f"{self.sno} - {self.title}"


  
    



@app.route('/products')
def products():
    return 'this is a product'

@app.route('/update/<int:sno>',methods=["GET","POST"])
def update(sno):
  if request.method=="POST":
      title=request.form["title"]
      desc=request.form["desc"]
      todo=Todo.query.filter_by(sno=sno).first()
      todo.title=title
      todo.desc=desc
      db.session.add(todo)
      db.session.commit()
      return redirect("/")
    
  todo=Todo.query.filter_by(sno=sno).first()
  return render_template('updates.html',todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

#creating main file to run
if __name__=="__main__":
  app.run(host='0.0.0.0', port=5000,debug=True)
  