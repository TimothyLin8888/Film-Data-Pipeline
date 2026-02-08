import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1-zjtBahGMRP-Ds7A2FG2umGFCjmxP6k8uU5DW5q5Yto"
workbook = client.open_by_key(sheet_id)

worksheet = workbook.get_worksheet(0)
sheets = worksheet.get('A1:D61')
for row in sheets:
    print(row)