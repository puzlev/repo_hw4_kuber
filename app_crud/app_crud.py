#from flask import Flask, jsonify        # Импорт Flask и функции jsonify
from flask import Flask
from config import Config
from models import db
from routes import bp

app = Flask(__name__)                   # Создание экземпляра Flask-приложения

#@app.route('/v2', methods=['GET'])      # Ответ по корневому пути
#def home():
#    return jsonify({"message": "Welcome to the home page! v2"})

#@app.route('/v2/health', methods=['GET']) # Определение маршрута для GET-запросов на /health/
#def health_check():                     # Функция, обрабатывающая запросы на /health/
#    return jsonify({"status": "OK"})    # Возвращает JSON-ответ {"status": "OK"}

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(bp)

#if __name__ == '__main__':              # Проверка, что скрипт выполняется как основная программа
#    app.run(host='0.0.0.0', port=8000)  # Запуск Flask-сервера на порту 8000

if __name__ == '__main__':
#    with app.app_context():
#        db.create_all()  # Создание всех таблиц
#    app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)  # Запуск на порту 8000
