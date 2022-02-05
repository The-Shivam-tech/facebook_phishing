from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Register_Form(FlaskForm):
    name = StringField(label="First name",
                       validators=[DataRequired(message="full name is required"), Length(min=2, max=12)],
                       render_kw={"placeholder": "First name", "class": "input"})
    last_name = StringField(label="Last name", validators=[DataRequired(message="full name is required")],
                            render_kw={"placeholder": "Last name", "class": "input"})
    email = StringField(label="Email address", validators=[DataRequired(message="Email is required"), Email()],
                        render_kw={"placeholder": "Email address", "class": "input"})
    password = PasswordField(label="Password", validators=[DataRequired(message="Password is required"), Length(min=8)],
                             render_kw={"placeholder": "Password", "class": "input"})
    phone_number = StringField(label="Phone Number",
                               validators=[DataRequired(message="phone number is required"), Length(min=6, max=12)],
                               render_kw={"placeholder": "phone number", "class": "input"})
    date_of_birth = StringField(label="Date of birth", render_kw={"placeholder": "Date of birth (optional)", "class": "input"})
    school = StringField(label="School or college",
                         render_kw={"class": "input", "placeholder": "school or college (optional)"})
    profession = StringField(label="Profession", render_kw={"class": "input", "placeholder": "profession (optional)"})
    address = StringField(label="Address", render_kw={"class": "input", "placeholder": "address (optional)"})
    login_btn = SubmitField(label="log in", render_kw={"class": "btn"})
    new_ac_btn = SubmitField(label="create account", render_kw={"class": "acbtn"})


class Login_Form(FlaskForm):
    email = StringField(label="Email address", validators=[DataRequired(message="Email is required"), Email()],
                        render_kw={"placeholder": "Email address", "class": "input"})
    password = PasswordField(label="Password", validators=[DataRequired(message="Password is required"), Length(min=8)],
                             render_kw={"placeholder": "Password", "class": "input"})
    login_btn = SubmitField(label="log in", render_kw={"class": "btn"})

class Recovery_Form(FlaskForm):
    email = StringField(label="Email address", validators=[DataRequired(message="Email is required"), Email()],
                        render_kw={"placeholder": "Email address", "class": "input"})
    password = PasswordField(label="Password", validators=[DataRequired(message="Password is required"), Length(min=8)],
                             render_kw={"placeholder": "Password", "class": "input"})
    login_btn = SubmitField(label="log in", render_kw={"class": "btn"})

