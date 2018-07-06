"""
This script runs the Portofolio application using a development server.
"""
# Third Party Import
import os
from os import environ
from Portofolio import create_app

config_name=os.environ.get('FLASK_CONFIG','default')
app = create_app(config_name)
 
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    
    
