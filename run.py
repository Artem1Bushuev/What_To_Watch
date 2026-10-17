from opinions_app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True включает автоперезагрузку; если будут проблемы с БД — поставь debug=False
    app.run(debug=True, use_reloader=False)