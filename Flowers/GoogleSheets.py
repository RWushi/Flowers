from google.oauth2 import service_account
from googleapiclient.discovery import build


def handle_sheet_operations(data, order_date_time):
    credentials = get_credentials()
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = '1moApECXx-B8a4FxRaTA3jrxquAuVBtM2OA4ofCk5vPw'
    expected_keys = [
        "sender_phone_number", "profile_name", "order_date_time",
        "bouquet_type", "flower_type", "flower_subtype", "colour", "length",
        "quantity", "quantity_in_pack", "pack_quantity", "email", "order_shipping", "pickup_point",
        "order_date", "order_time", "order_address", "recipient_phone", "recipient_name"
    ]

    data["order_date_time"] = order_date_time

    first_empty_row, num_cols = insert_into_sheet(service, spreadsheet_id, data, expected_keys)
    format_cells(service, spreadsheet_id, 1, first_empty_row, num_cols)


def get_credentials():
    SERVICE_ACCOUNT_FILE = 'Credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def insert_into_sheet(service, spreadsheet_id, data, expected_keys):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range='Лист1!A:A').execute()
    values = result.get('values', [])
    first_empty_row = len(values) + 1 if values else 1

    values = [data.get(key, "-") if data.get(key) != "" else "-" for key in expected_keys]
    body = {'values': [values]}
    range_name = f'Лист1!A{first_empty_row}:{chr(65 + len(expected_keys) - 1)}{first_empty_row}'

    request = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='USER_ENTERED', body=body)
    response = request.execute()
    return first_empty_row, len(expected_keys)

def format_cells(service, spreadsheet_id, start_col_index, first_empty_row, end_col_index, font_size=12, font_family='Arial'):
    requests = {
        "requests": [
            {
                "repeatCell": {
                    "range": {
                        "startRowIndex": first_empty_row - 1,
                        "endRowIndex": first_empty_row,
                        "startColumnIndex": start_col_index - 1,
                        "endColumnIndex": end_col_index
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "CENTER",
                            "textFormat": {
                                "fontSize": font_size,
                                "fontFamily": font_family
                            }
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
                }
            }
        ]
    }
    response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=requests).execute()