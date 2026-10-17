"""CLI-команды для загрузки данных."""

import csv

import click

from . import db
from .models import Opinion


def register_cli_commands(app):
    @app.cli.command("load_opinions")
    def load_opinions_command():
        """Загружает мнения из opinions.csv в базу данных."""
        csv_path = (
            "opinions.csv"  # путь относительно текущей рабочей директории
        )
        counter = 0
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                opinion = Opinion(**row)
                db.session.add(opinion)
                db.session.commit()
                counter += 1
        click.echo(f"Загружено мнений: {counter}")
