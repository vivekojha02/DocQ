from flask import Flask, render_template, request, redirect, session, flash, url_for
from utils.otp_handler import generate_otp, validate_otp, otp_request_tracker
from utils.email_sender import send_otp_email, send_confirmation_email
from utils.google_sheets import check_existing_booking, save_appointment, cancel_appointment
from config import *
from datetime import datetime, timedelta
import re

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.permanent_session_lifetime = PERMANENT_SESSION_LIFETIME

# ------------------------------
# Routes
# ------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        session['email'] = email

        # OTP logic with limits
        if not otp_request_tracker.allow(email):
            flash("Oh no ! You have exceeded OTP limit. Try again later dear.", "danger")
            return render_template('index.html')

        otp = generate_otp(email)
        send_otp_email(email, otp)
        flash("OTP sent to your email.", "info")
        return redirect(url_for('verify'))

    return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        otp_input = request.form['otp']
        if validate_otp(session.get('email'), otp_input):
            session['authenticated'] = True
            return redirect(url_for('book'))
        else:
            flash("Invalid or expired OTP.", "danger")

    return render_template('verify.html')

@app.route('/resend_otp', methods=['POST'])
def resend_otp():
    email = session.get('email')
    if not email:
        return {'message': 'Session expired. Please re-enter your email.'}, 400

    # Generate and send a new OTP
    otp = generate_otp(email)
    send_otp_email(email, otp)
    return {'message': 'New OTP sent to your email.'}


@app.route('/book', methods=['GET', 'POST'])
def book():
    if not session.get('authenticated'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name'].strip()
        age = request.form['age']
        gender = request.form['gender']
        contact = request.form['contact']
        email = session['email']
        date = request.form['date']
        time = request.form['time']
        doctor = request.form['doctor']
        symptoms = request.form.get('symptoms')
        appointment_type = request.form['appointment_type']
        previous_visit = request.form.get('previous_visit')

        today = datetime.today().strftime('%Y-%m-%d')
        if date < today:
            flash("Sorry we can't go in past😒 You can't book past dates!", "warning")
            return render_template('book.html')

        # Enforce only 1 booking per day per name
        if check_existing_booking(name, date):
            flash("You already have a confirmed appointment for this date😊.", "warning")
            return render_template('book.html')

        # Save to Google Sheets
        save_appointment({
            'name': name,
            'age': age,
            'gender': gender,
            'contact': contact,
            'email': email,
            'date': date,
            'time': time,
            'doctor': doctor,
            'symptoms': symptoms,
            'type': appointment_type,
            'previous_visit': previous_visit
        })

        send_confirmation_email(email, name, date, time, doctor)
        flash("Appointment booked successfully.", "success")
        return render_template('success.html', name=name, date=date, time=time)

    return render_template('book.html')

@app.route('/cancel', methods=['POST'])
def cancel():
    name = request.form['name']
    date = request.form['date']

    result = cancel_appointment(name, date)
    if result:
        flash("Appointment cancelled.", "info")
    else:
        flash("No matching appointment found.", "danger")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)