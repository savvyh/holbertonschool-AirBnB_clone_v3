#!/usr/bin/python3
"""variables and methods used to connect to API"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''Returns a JSON error 404'''
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
