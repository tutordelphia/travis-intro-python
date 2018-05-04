import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)


def start():
	print("Starting server at http://localhost:" + str(PORT))
	httpd.serve_forever()

if __name__ == "__main__":
	start()
