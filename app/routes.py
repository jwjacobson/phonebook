from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SubmissionForm, SignUpForm, LoginForm
from app.models import Entry, User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submission', methods = ['GET', 'POST'])
def submission():
    form = SubmissionForm()
    if form.validate_on_submit():
        print("Validated.")
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        print(first_name, last_name, phone_number, address)
        new_entry = Entry(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
        flash(f"{first_name} {last_name}'s data successfully registered.", "info")
        return redirect(url_for('index'))
    return render_template('submission.html', form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Validated.')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password)
        check_user = db.session.execute(db.select(User).filter((User.username == username) | (User.email == email))).scalars().all()
        if check_user:
            flash("User already exists", "dark")
            return redirect(url_for('signup'))
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        flash(f"User {new_user.username} created.", "info")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Validated.')
        username = form.username.data
        password = form.password.data
        print(username, password)
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'Logged in as {username}', 'info')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials.', 'dark')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f"Logged out", "info")
    return redirect(url_for('index'))