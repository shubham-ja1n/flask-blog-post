from flask import render_template, url_for, request, flash, redirect, Blueprint
from flask_login import login_required, logout_user, login_user
from myblogposts import db
from myblogposts.models import User
from myblogposts.users.forms import LoginForm, RegisterForm, UpdateForm

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login Successful')
            next = request.args.get('next')
            if next==None or not next[0] == '/':
                next = url_for('core.home')
            return redirect(next)
    return render_template('login.html', form=form)

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('registration.html', form=form)

@login_required
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.home'))