"""
The flask application package.
"""

from flask import Flask
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

def init_mysql():
    # open credentials file and edit mysql.config
    pass

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''

mysql.init_app(app)

import BucketListApp.views
