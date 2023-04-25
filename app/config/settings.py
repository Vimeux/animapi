import os

from dotenv import load_dotenv

load_dotenv()

# Flask settings
HOST = os.getenv('FLASK_HOST', '0.0.0.0')
PORT = os.getenv('FLASK_PORT', 5000)
DEBUG = os.getenv('FLASK_DEBUG', False)

# MongoDB settings
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'test')

