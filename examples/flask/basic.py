from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from wtforms_sqlalchemy.orm import model_form

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Make(db.Model):
    __tablename = 'make'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __str__(self):
        return self.name


class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    make_id = db.Column(db.Integer, db.ForeignKey('make.id'))
    model = db.Column(db.String(50))

    make = db.relationship(Make)

    def __str__(self):
        return ' '.join((str(self.year), str(self.make), self.model))


MakeForm = model_form(Make, db_session=db.session)
CarForm = model_form(Car, db_session=db.session)


@app.route('/make', methods=['GET', 'POST'])
def make():
    make = Make()
    success = False

    if request.method == 'POST':
        form = MakeForm(request.form, obj=make)
        if form.validate():
            form.populate_obj(make)
            db.session.add(make)
            db.session.commit()
            success = True
    else:
        form = MakeForm(obj=make)

    return render_template('create.html', model=Make, form=form, success=success)


@app.route('/', methods=['GET', 'POST'])
def car():
    car = Car()
    success = False

    if request.method == 'POST':
        form = CarForm(request.form, obj=car)
        if form.validate():
            form.populate_obj(car)
            db.session.add(car)
            db.session.commit()
            success = True
    else:
        form = CarForm(obj=car)

    return render_template('create.html', model=Car, form=form, success=success)


if __name__ == '__main__':
    db.create_all()

    app.run(debug=True)
