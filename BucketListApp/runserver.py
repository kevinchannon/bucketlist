"""
This script runs the BucketListApp application using a development server.
"""

from os import environ

from BucketListApp import app, init_mysql

if __name__ == '__main__':
    if init_mysql():
        HOST = environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555

        app.run(HOST, PORT)
    else:
        print "Failed to intialise DB"
