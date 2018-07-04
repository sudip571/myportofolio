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
    print(app.config['EMAIL_RECEIVER'])
    print(app.config['TOP_LEVEL_DIR'])    
    app.run()
    
