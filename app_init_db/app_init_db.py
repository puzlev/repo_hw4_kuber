from flask import Flask
from config import Config
from models import db

app = Flask(__name__)           # Создание экземпляра Flask-приложения

app.config.from_object(Config)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()         # Создание всех таблиц
