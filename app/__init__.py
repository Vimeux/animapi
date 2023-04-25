from flask import Flask
from flask_cors import CORS
from app.config import settings
from app.routes import anime_blueprint

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = settings.MONGO_URI

app.register_blueprint(anime_blueprint)