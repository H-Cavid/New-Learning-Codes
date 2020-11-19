from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)
class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(70))
    author=db.Column(db.String(70))

@app.route('/')
def booklist():
    booklist=Book.query.all()
    return render_template("booklist.html",list=booklist)

@app.route('/add',methods=["GET","POST"])
def addbook():
    if request.form:
        bookname=request.form['bookName']
        authorname=request.form['authorName']
        book=Book(name=bookname,author=authorname)
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("addbook.html")

@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    return render_template("update.html")

@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)