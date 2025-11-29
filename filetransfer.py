import http.server
import socketserver

port = 8080  
myHandler = http.server.SimpleHTTPRequestHandler

print("Starting file server.")

with socketserver.TCPServer(("", port), myHandler) as srv:
    print("Server running at port", port)
    print("CTRL+C to stop")
    srv.serve_forever()
