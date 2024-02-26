def create_app():
    from flask import Flask
    from dotenv import load_dotenv
    import os

    load_dotenv()

    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.environ.get("SECRET_KEY"))

    from .handlers import bp_users
    app.register_blueprint(bp_users)

    return app
