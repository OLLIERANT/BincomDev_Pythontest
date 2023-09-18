#!/usr/bin/python3
"""
Creates a page to be used
to store results for 
ALL parties for a new polling unit.
"""

import MySQLdb
import http.server
import socketserver
import cgi
import sys

#  MySQL database configuration settings
db_config = {
        'host': "localhost",
        'db': "bincomphptest",
        'user': "root",
        'passwd': "root"
}

db = MySQLdb.connect(db_config)
cursor = db.cursor()

#  Define the port for web server to the available port not in use
PORT = 0

# Create a custom request handler
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse the POST data to get the results for all parties
        form = cgi.FieldStorage(fp=cgi.StringIO(post_data), environ=self.environ)
        
        # Store the results in your database
        for field in form:
            party_name = field
            party_score = form[field].value

            # Insert the data into your database
            sql = "INSERT INTO results (party_name, party_score) VALUES (%s, %s)"
            val = (party_name, party_score)
            cursor.execute(sql, val)
            db.commit()
			cursor.close

            print(f"Received result for {party_name}: {party_score}. Inserted into database.")
	
	# Respond to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Results saved successfully')

# Create an HTTP server with the custom request handler
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
