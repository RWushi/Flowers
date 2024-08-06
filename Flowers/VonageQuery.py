from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import base64
from GoogleSheets import handle_sheet_operations
from GetData import get_data_by_category
from datetime import datetime
import pytz


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        action = self.headers.get('Action')
        category_names_header = self.headers.get('Category-Names')

        if action == 'GET':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            encoded_category_names = category_names_header.split(',')
            category_names = [base64.b64decode(name).decode('utf-8') for name in encoded_category_names]
            print(category_names)
            data = get_data_by_category(category_names)

            if "Оформление" in category_names:
                formatted_data = json.loads(data)
                formatted_data['tab'] = '\r\n'
                response = json.dumps(formatted_data, ensure_ascii=False)
                print(formatted_data)
            else:
                response = json.dumps(data, ensure_ascii=False)

            self.wfile.write(response.encode('utf-8'))

        elif action == 'POST':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))

                almaty_tz = pytz.timezone('Asia/Almaty')
                current_time = datetime.now(almaty_tz).strftime("%d.%m.%Y %H:%M:%S")

                handle_sheet_operations(data, current_time)
                self.send_response(200)
                self.end_headers()
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(400)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()