# import module http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class SimpleHTTP(BaseHTTPRequestHandler):

    # Nhan GET request gui len
    def do_GET(self):
        # SET http status tra ve
        self.send_response(200)

        #Thiet lap header tra ve
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # Data
        message = "Hoc Lap Trinh Tai Toidicode.com"

        #Write data duoi dang utf8
        self.wfile.write(bytes(message, "utf8"))
        return

# cau hinh host va cong port cho server
server_address = ('127.0.0.1', 8000)

http = HTTPServer(server_address, SimpleHTTP)

http.server_forever()




