"""Инициализация приложения и настройка базы данных."""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Создать экземпляр приложения Flask и настроить его."""
    app = Flask(__name__)

    # Самое важное: секретный ключ для CSRF и сессий
    app.config["SECRET_KEY"] = "dev-key-change-in-production"  # <-- добавь эту строку

    # Определяем корень проекта
    project_root = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(project_root)

    instance_path = os.path.join(project_root, "instance")
    os.makedirs(instance_path, exist_ok=True)

    db_path = os.path.join(instance_path, "app.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .models import Opinion  # noqa: F401
    from .views import bp as views_bp

    app.register_blueprint(views_bp)

    with app.app_context():
        db.create_all()

    return app
