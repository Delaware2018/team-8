import os

from app import create_app
from flask_cors import CORS
CORS(app)

config_name = "development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
