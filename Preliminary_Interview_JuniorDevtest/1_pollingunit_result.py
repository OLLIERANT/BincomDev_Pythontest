#!/usr/bin/python3
"""
Script that creates a web page
to display the result for 
any individual polling unit.
"""

#  Make sure to have MySQLdb package installed for Python
pip install MySQL-python


import MySQLdb
import http.server
import socketserver
import sys

#  MySQL database configuration settings based on my test environment
db_config = {
        'host': "localhost",
        'db': "bincomphptest",
        'user': "root",
        'passwd':"root"
}

#  Function to fetch the result for a specific polling unit
def get_polling_unit_results(polling_unit_id):
    try:
        connection = MySQLdb.connect(db_config)
        cursor = connection.cursor()
        
        query = """
        SELECT *
        FROM announced_pu_results
        WHERE polling_unit_uniqueid = 8
        """
        cursor.execute(query, (polling_unit_id,))
        results = cursor.fetchall()
        connection.close()
        return results
    except MySQLdb.Error as e:
        return f"MySQL Error: {e}"

#  Create a simple HTML webpage to display the results
def create_html_page(results):
    html_content = "<html><head><title>Polling Unit Results</title></head><body>"
    html_content += "<h1>Polling Unit Results</h1>"

    if results:
        html_content += "<table>"
        html_content += "<tr><th>Party</th><th>Votes</th></tr>"
        for row in results:
            html_content += f"<tr><td>{row[2]}</td><td>{row[3]}</td></tr>"
        html_content += "</table>"
    else:
        html_content += "<p>No results found for this polling unit.</p>"

    html_content += "</body></html>"
    return html_content

class PollingUnitHandler(http.server.BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        polling_unit_id = self.path.split("/")[-1]
        results = get_polling_unit_results(polling_unit_id)
        html_page = create_html_page(results)

        self.wfile.write(bytes(html_page, "utf-8"))

if __name__ == ""__main__"":
    #  can change to desired port
    port = 8000
    with socketserver.TCPServer(("", port), PollingUnitHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()
