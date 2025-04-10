from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stayH4rdJob&Fer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Congrats(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fiance = db.Column(db.String(10), nullable = False)
    congrat = db.Column(db.String(1000), nullable = False)
    person = db.Column(db.String(50), nullable = False)

@app.route('/')
def home():
    return render_template('std.html')

@app.route('/std', methods = ['GET', 'POST'])
def std():
    if request.method == 'POST':
        fiance = request.form.get('fiance')
        person = request.form.get('person')
        congrat = request.form.get('congrat')

        new_congrat = Congrats(
            fiance = fiance,
            person = person,
            congrat = congrat
        )

        db.session.add(new_congrat)
        db.session.commit()
        flash('Felicitaciones enviadas, gracias !', 'success')


        return redirect(url_for('std'))
    return render_template('std.html')

if __name__ == '__main__':
    app.run(debug=True)