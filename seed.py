from opinions_app import create_app, db
from opinions_app.models import Opinion
from datetime import datetime, timezone
now = datetime.now(timezone.utc)

app = create_app()

with app.app_context():
    # Очищаем таблицу, чтобы не дублировать записи при повторном запуске
    Opinion.query.delete()

    now = datetime.utcnow()

    db.session.add(Opinion(
        title="Отличный фильм",
        text="Отличное кино, очень советую!",
        source="user_review",
        timestamp=now,
        added_by="admin"
    ))
    db.session.add(Opinion(
        title="Неплохой фильм, но с оговорками",
        text="Неплохо, но концовка подкачала.",
        source="user_review",
        timestamp=now,
        added_by="admin"
    ))
    db.session.add(Opinion(
        title="Скучновато",
        text="Скучновато, не досмотрел.",
        source="user_review",
        timestamp=now,
        added_by="admin"
    ))

    db.session.commit()
    print("✅ Тестовые записи добавлены!")
