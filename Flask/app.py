from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
app.secret_key = "Secret_Key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" 

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return '{name:'+self.name+', email:'+str(self.email)+ '}'

@app.route('/')
def index():
    allPersons = Person.query.all()
    return render_template("index.html", persons = allPersons)

@app.route('/insert', methods = ['POST'])
def insert():
    # name, surname, email
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    newPerson = Person(name, email, phone)
    db.session.add(newPerson)
    db.session.commit()
    flash("Məlumat daxil oldu. Təşəkkürlər")
    return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET'])
def delete(id):
    selectedPerson = Person.query.get(id)
    db.session.delete(selectedPerson)
    db.session.commit()
    flash("Məlumat silindi. Təşəkkürlər")
    return redirect(url_for("index"))

@app.route('/edit/<id>', methods = ['POST'])
def edit(id):
    selectedPerson = Person.query.get(id)
    selectedPerson.name = request.form['name']
    selectedPerson.email = request.form['email']
    selectedPerson.phone = request.form['phone']
    db.session.commit()
    flash("Məlumat dəyişdirildir. Təşəkkürlər")
    return redirect(url_for("index"))