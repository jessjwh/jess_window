from flask import Blueprint,render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,StringField,SelectField,BooleanField,DateField,TextAreaField
from wtforms.validators import DataRequired,Length,Regexp,Optional,EqualTo
from .datasource import validateUser,insert_data,InvalidEmailException
import datetime,secrets
from werkzeug.security import generate_password_hash, check_password_hash
auth_blueprint = Blueprint('auth',__name__)


class UserRegistrationForm(FlaskForm):
    uName = StringField('Name', validators=[DataRequired(), Length(min=2, max=10)])
    uSex = SelectField('Sex', choices=[("M","M"), ("F","F")])
    uMobile = StringField('Mobile', validators=[DataRequired(), Regexp(r'\d\d\d\d-\d\d\d-\d\d\d', message="Incorrect format")])
    uEmail = EmailField("Email", validators=[DataRequired()])
    isGetEmail = BooleanField("Receive marketing emails", default=False)
    uBirth = DateField("Birth", validators=[Optional()], format='%Y-%m-%d')
    uAboutMe = TextAreaField("Self Introduction", validators=[Optional(), Length(max=200)], description="Max 200 characters")
    uPass = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=20), EqualTo('uConfirmPass', message='Incorrect password')])
    uConfirmPass = PasswordField("Verify Password", validators=[DataRequired(), Length(min=4, max=20)])

@auth_blueprint.route('/auth/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm
    if request.method == "POST":
        if form.validate_on_submit():
            uName = request.form['uName']
            print("Name=", uName)

            uSex = form.uSex.data
            print("Sex=", uSex)

            uMobile = form.uMobile.data
            print("Mobile=", uMobile)

            uEmail = form.uEmail.data
            print("Email=", uEmail)

            isGetEmail = form.isGetEmail.data
            print("MarketingEmail=", "Yes" if isGetEmail else "No")

            uBirth:datetime.date | None = form.uBirth.data
            if uBirth is not None:
                uBirth_str = uBirth.strftime("%Y-%m-%d")
                print("Birth=", uBirth_str)
            else:
                uBirth_str = "1977-07-07"

            uAboutMe = form.uAboutMe.data
            print("AboutMe=", uAboutMe)

            uPass = form.uPass.data
            print("Password=", uPass)

            # Password Hash
            hash_password = generate_password_hash(uPass, method= 'pbkdf2:sha256', salt_length=8)
            print("Hash=", hash_password)
            conn_token = secrets.token_hex(16)
            print("Token=", conn_token)

            try:
                insert_data([uName, uSex, uMobile, uEmail, isGetEmail, uBirth_str, uAboutMe, uPass, hash_password, conn_token])
            except InvalidEmailException:
                form.uEmail.errors.append("Email already existed")
            except Exception as e:
                print(e)
                form.uEmail.errors.append("Unknown errors")
            else:
                return redirect(f'/auth/login/{uEmail}')

    else:
        print("First entry")

    return render_template('/auth/register.html.jinja', form=form)

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=4, max=20)])


@auth_blueprint.route("/auth/", methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login/", methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login/<email>")
def index(email:str | None = None):
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("Form submitted")
            print("Token verified")
            email = form.email.data
            password = form.password.data
            print(f'email: {email}')
            print(f'password: {password}')
            is_ok, username = validateUser(email, password)
            if is_ok:
                session['username'] = username
                return redirect('/')
            else:
                form.email.errors.append("Incorrect email or password")
                form.email.data = ""

    else:
        print("New Entry")
        if email is not None:
            form.email.data = email
    
    return render_template('/auth/login.html.jinja',form=form)

@auth_blueprint.route("/auth/logout")
def logout():
    session.pop('username')
    return redirect('/')