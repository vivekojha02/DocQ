# utils/google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import SHEET_NAME, SERVICE_ACCOUNT_FILE, get_worksheet


# Authorize client
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(credentials)
sheet = client.open(SHEET_NAME).sheet1

def save_appointment(data):
    row = [
        data['name'],
        data['age'],
        data['gender'],
        data['contact'],
        data['email'],
        data['date'],
        data['time'],
        data['doctor'],
        data.get('symptoms', ''),
        data['type'],
        data.get('previous_visit', '')
    ]
    sheet.append_row(row)
    
def check_existing_booking(name, date):
    worksheet = get_worksheet()
    data = worksheet.get_all_records()

    for row in data:
        if 'name' in row and 'date' in row:
            if row['name'].strip().lower() == name.strip().lower() and row['date'] == date:
                return True
    return False


def cancel_appointment(name, date):
    records = sheet.get_all_records()
    for i, row in enumerate(records, start=2):  # Start from 2 because of header
        if row['name'].strip().lower() == name.strip().lower() and row['date'] == date:
            sheet.delete_row(i)
            return True
    return False
