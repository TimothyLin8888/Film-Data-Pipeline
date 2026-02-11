import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_SHEET_ID, WORKSHEET_NAME
from gspread.utils import rowcol_to_a1

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("../credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = GOOGLE_SHEET_ID
workbook = client.open_by_key(sheet_id)

def write(info: dict, start_cell: str = "A1", worksheet_name: str = WORKSHEET_NAME):
    worksheet = None

    try:
        worksheet = workbook.worksheet(worksheet_name)
    except gspread.WorksheetNotFound:
        worksheet = workbook.add_worksheet(title=WORKSHEET_NAME, rows=100, cols=20)

    headers = list(info.keys())
    columns = list(info.values())

    row_count = len(columns[0])

    rows = []

    for i in range(row_count):
        rows.append([col[i] for col in columns])


    data = [headers] + rows
    end_row = len(data)
    end_col = len(headers)

    if worksheet.row_count < end_row:
        worksheet.resize(rows=end_row)

    end_cell = rowcol_to_a1(end_row, end_col)
    worksheet.update(f"{start_cell}:{end_cell}", rows)
