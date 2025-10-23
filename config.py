import os
from datetime import timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Define the path to your Google service account JSON
GOOGLE_CREDS_FILE = "credentials/service_account.json"

# Load credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDS_FILE, scope)
client = gspread.authorize(creds)

def get_worksheet():
    sheet = client.open(SHEET_NAME)
    return sheet.sheet1  # or specify a sheet name if needed

# -------------------------------
# Flask Config
# -------------------------------
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'Shash@nk3018')
PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)  # Session timeout after 10 minutes

# -------------------------------
# Gmail SMTP Config for OTP + Confirmation
# -------------------------------
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'envy9197@gmail.com'           # Change this to your Gmail address
EMAIL_HOST_PASSWORD = 'dqcd elid lgdx bxqp'     # App password generated from Gmail
OTP_VALIDITY_MINUTES = 2
OTP_RESEND_LIMIT = 3

# -------------------------------
# Google Sheets Config
# -------------------------------
GOOGLE_SHEET_ID = '1t_Ayj4fpv4sXqZtBDxP77Nk9IibFFidFguhmEkAfvCk'       # Sheet ID from Google Sheets URL
SHEET_NAME = 'Appointments'                         # Sheet/tab name

# -------------------------------
# Booking Limits
# -------------------------------
MAX_APPOINTMENTS_PER_DAY = 1                        # Only 1 appointment per day allowed
ALLOWED_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
GENERAL_START_TIME = '09:00'
GENERAL_END_TIME = '13:00'
EVENING_START_TIME = '17:00'
EVENING_END_TIME = '21:00'
SUNDAY_END_TIME = '13:00'

# -------------------------------
# Emergency Handling
# -------------------------------
ALLOW_EMERGENCY_BOOKING = True
EMERGENCY_NOTICE = "For emergency cases, please visit the clinic directly or call our helpline."

# -------------------------------
# Service Account (Google Sheets)
# -------------------------------
SERVICE_ACCOUNT_FILE = os.path.join('credentials', 'service_account.json')
# -------------------------------
# OTP Throttling Control
# -------------------------------
MAX_OTP_REQUESTS = 3               # Max OTP requests allowed per session
OTP_COOLDOWN_SECONDS = 120        # 2-minute wait between OTPs

# -------------------------------
# SMTP Alias for Utility Access
# -------------------------------
SMTP_EMAIL = EMAIL_HOST_USER
SMTP_PASSWORD = EMAIL_HOST_PASSWORD
# -------------------------------
# Service Account (Google Sheets)
# -------------------------------
SERVICE_ACCOUNT_FILE = os.path.join('credentials', 'service_account.json')
GOOGLE_CREDS_FILE = SERVICE_ACCOUNT_FILE
