"""
The flask application package.
"""

import os
import json
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

def init_mysql():
    # open credentials file and edit mysql.config

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    credentials_path = os.path.join( SITE_ROOT, "Credentials.json")

    print "Looking for DB credentials in ", credentials_path

    with open(credentials_path) as credentials_file:
        json_string = credentials_file.read()
        credentials = json.loads(json_string)
        if "user" not in credentials:
            return False
        if "password" not in credentials:
            return False
        if "database" not in credentials:
            return False
        if "host" not in credentials:
            return False

        #MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = credentials["user"]
        app.config['MYSQL_DATABASE_PASSWORD'] = credentials["password"]
        app.config['MYSQL_DATABASE_DB'] = credentials["database"]
        app.config['MYSQL_DATABASE_HOST'] = credentials["host"]

        return True

    mysql.init_app(app)

import BucketListApp.views
