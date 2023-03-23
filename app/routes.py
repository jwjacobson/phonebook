from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
from app.models import User

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
        flash(f"{first_name} {last_name}'s data successfully registered.", "primary")
        return redirect(url_for('index'))
    return render_template('submission.html', form=form)
