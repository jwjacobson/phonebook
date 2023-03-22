from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submission', methods = ['GET', 'POST'])
def submission():
    form = SignUpForm()
    if form.validate_on_submit():
        print("Validated.")
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        print(first_name, last_name, phone_number, address)
        flash(f"{first_name}'s data successfully registered!", "primary")
        return redirect(url_for('index'))
    return render_template('submission.html', form=form)
