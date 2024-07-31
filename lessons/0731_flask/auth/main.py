from flask import Blueprint,render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Length
from .datasource import validateUser
auth_blueprint = Blueprint('auth',__name__)

class LoginForm(FlaskForm):
    email = EmailField('Email: ',validators=[DataRequired()])
    password = PasswordField('Password: ',validators=[DataRequired(), Length(min=4, max=20)])


@auth_blueprint.route("/auth/", methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("表單傳送過來")
            print("驗證了token")
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
    
    return render_template('/auth/login.html.jinja',form=form)

@auth_blueprint.route("/auth/logout")
def logout():
    session.pop('username')
    return redirect('/')