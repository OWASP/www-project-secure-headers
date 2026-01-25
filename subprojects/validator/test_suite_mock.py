"""
Simple mock endpoint returning a HTTP response, for which, all HTTP response headers recommended by the OSHP will be set.

Dependencies:
    pip install requests flask

References:
    https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application

Run (PowerShell):
    PS> $env:FLASK_ENV = "production"
    PS> $env:FLASK_APP = "test_suite_mock"
    PS> flask run --host=localhost --port=80 --eager-loading --no-reload --no-debugger --with-threads
"""
import io
import requests
import base64
from flask import Flask, Response, send_file

OSHP_HTTP_HEADERS_JSON_REF = "https://raw.githubusercontent.com/OWASP/www-project-secure-headers/master/ci/headers_add.json"
FAVICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADV0lEQVRYhd2W70sTcRzHj6SCetIfEGTuNAj6AUVFBD2K6EnPDIIeVEql32VWaARR04h2kyJqBY5iUv7YffO2SpIyyLayWmVuO39ket8zxXS7uX0XVFDZpwfbzc1WO2tq9IX3g7sH9359ft6XYTJwiuw5e5DAhpHAEtSYuz4T39R89lWvmYsE3UcksBDTwxkFyMdMFhJ0IRWguJFtnlEAhmEYvUO3DQmsB9nZVmTPyZtxgFk5xXb2cLGgOzprAEhgh5CgG5lFgKVLSh3Z2TNm2NA/trGejG2ZLE70/6yu4LqMA2A50oUJhUTxUhhMopJK7v8PgJeoERP6NC2AL+DiRMWQcYAoRHhvOgCjGNgxLeb/HEBD3wBUP+fg4K21UHa/EM56+qcXwGAwzMFy5J4KYHFzcOnRHvUPCGUtRbEsBOzTAsBL9Fhi+i+7UBLAoTubExsRZdTcJkc2YEK/JAJY3FVJAOUt+sRe+Gzs9K/KiLlDDi/iSVievANsfYNgcZ+DktsboaylGIweMrkhe6q8owv/GgATejNqGoYa7x2wdjQALwXSLaKoOoPWvzLnZXpAjbi2+zmYnQVgdhaA1dOoDUBUoEr07/qzyKXQCkzoJxWgvrcHzM59YHYWwHXx4QSAzw+GZ41Q/qAEjjbvgLL7hXDCZYazHb0qxAdTdyB3SuZN72FBqt1f3/sW6t744s83ul9CadNWSLiQxqW3L4dTbbUqRPvF5r752qMn9ComFGz9w3CtvQbqejqAl0KxqENQ29MOlhfnk6YgJYRjBZxpfx2DCF7QZM7LkZ1q01ncVfG6m1374cqTI3DZdSD+Lh0AElg4fHc7cL4RMInKd847uv235rZBqsOERjChYO3AE+a/kBYAJLBwvPW0moUg5x1bnDrtXTAPS/RltOPdYHYWZgwACXlQ6W6JTYXixABZKeoeORet+whceVya1nxqACyU3N4EnHcoth+UimRzObwaEzqOCYUab5Mm86kCIIGFk0+s6lR85bzDyyYaj4Qr46PV1ZbUaJkC0DtWQqW7OXFLliekP6RPmnkpBLb+UU0yegbSyzsAnM8/+eq2Ow5Q/erVXF4KcZjQISzTb1iOjGsRT+i4qTOoXT7lGycq70ydSkU+xlkMwzA/AGJ0YgsiILrEAAAAAElFTkSuQmCC"
app = Flask(__name__)


def load_headers():
    oshp_headers = {}
    resp = requests.get(OSHP_HTTP_HEADERS_JSON_REF, timeout=60)
    headers = resp.json()["headers"]
    for header in headers:
        oshp_headers[header["name"]] = header["value"]
    return oshp_headers


@app.route("/favicon.ico")
def get_favicon():
    return send_file(io.BytesIO(base64.b64decode(FAVICON_B64)), mimetype="image/jpg")


@app.route('/')
def mirror():
    oshp_headers = load_headers()
    resp = Response(response="OK", headers=oshp_headers, content_type="text/plain")
    return resp

