import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # папка opinions_app
INSTANCE_FOLDER = os.path.join(os.path.dirname(BASE_DIR), "instance")


class Config(object):
    # Абсолютный путь к БД — SQLite точно поймёт, куда писать
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_FOLDER, 'db.sqlite3')}"
    SECRET_KEY = os.getenv("SECRET_KEY", "MY_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
