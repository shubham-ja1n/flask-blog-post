from flask import render_template, url_for, request, flash, redirect, Blueprint
from flask_login import login_required, logout_user, login_user, current_user
from myblogposts import db
from myblogposts.models import User, BlogPost
from myblogposts.users.forms import LoginForm, RegisterForm, UpdateForm
from myblogposts.users.picture_handler import add_profile_picture

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

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.home'))

@users.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            pic = add_profile_picture(form.picture.data, current_user.username)
            current_user.profile_image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', form=form, profile_image=profile_image)

@users.route('/<username>')
@login_required
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_post=blog_posts, user=user)