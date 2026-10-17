"""Представления (views) приложения."""

from random import randrange

from flask import Blueprint, flash, redirect, render_template, url_for

from opinions_app import db

from .forms import OpinionForm
from .models import Opinion

bp = Blueprint("views", __name__)


@bp.route("/")
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        # Если мнений нет — показываем шаблон с сообщением «Пока нет мнений»
        return render_template("opinion.html", opinion=None)

    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template("opinion.html", opinion=opinion)


@bp.route("/add", methods=["GET", "POST"])
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        # Проверка на дубликат по тексту
        if Opinion.query.filter_by(text=text).first() is not None:
            flash("Такое мнение уже было оставлено ранее!", "warning")
            return render_template("add_opinion.html", form=form)

        opinion = Opinion(
            title=form.title.data,
            text=text,
            source=form.source.data,
        )
        db.session.add(opinion)
        db.session.commit()
        flash("Мнение успешно добавлено!", "success")
        return redirect(url_for("views.opinion_view", id=opinion.id))

    return render_template("add_opinion.html", form=form)


@bp.route("/opinion/<int:id>")
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template("opinion.html", opinion=opinion)
