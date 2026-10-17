from opinions_app import create_app, db

app = create_app()
with app.app_context():
    uri = app.config["SQLALCHEMY_DATABASE_URI"]
    print(f"📂 URI базы данных: {uri}")

    # Для Windows дополнительно покажем абсолютный путь к файлу
    from urllib.parse import urlparse

    parsed = urlparse(uri)
    if parsed.scheme == "sqlite":
        path = parsed.path
        # Убираем начальный слэш, если есть, чтобы корректно склеить с Windows-путями
        if path.startswith("/"):
            path = path[1:]
        import os

        abs_path = os.path.abspath(path)
        print(f"📍 Абсолютный путь к файлу БД: {abs_path}")

    print("🚀 Начинаем создание таблиц...")
    db.create_all()
    print("✅ База данных и таблица 'opinion' созданы!")
