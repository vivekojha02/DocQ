# utils/email_sender.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_EMAIL, SMTP_PASSWORD

def send_otp_email(recipient, otp):
    subject = "Your OTP for Doctor Appointment Confirmation"
    body = f"""
    Dear Patient,
    
    Thank You for choosing us,

    Your OTP is: {otp}
    It is valid for 5 minutes. Please enter it on verification page to complete your booking.
    
    DO NOT SHARE OTP WITH ANYONE

    Regards,
    Sinha Clinic Support Team,
    Near Priyam Plaza, Ruchi Khand ,Lucknow ,UP
    """

    print(f"📤 Sending OTP {otp} to {recipient}")
    send_email(recipient, subject, body)

def send_confirmation_email(recipient, name, date, time, doctor):
    subject = "Appointment Confirmed - Sinha Clinic"
    body = f"""
    Dear {name},

    Your appointment has been confirmed.

    Date: {date}
    Time: {time}
    Doctor: {doctor}
    You Have choosen to pay fee in offline mode 

    Please visit clinic 10 minutes early.
    
    Need to make a change ?
      Reschedule or Cancel your Appointment by sending a reply to mail.
    
    Buy medicines at 30% discount

    Regards,
    Sinha Clinic Support Team,
    Near Priyam Plaza, Ruchi Khand ,Lucknow ,UP
    """

    print(f"📤 Sending appointment confirmation to {recipient} for {date} at {time}")
    send_email(recipient, subject, body)

def send_email(to_address, subject, body):
    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, to_address, msg.as_string())
        server.quit()
        print(f"✅ Email successfully sent to {to_address}")
    except Exception as e:
        print("❌ Email failed to send:", e)
