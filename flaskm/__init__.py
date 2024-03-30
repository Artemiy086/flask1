def create_app():
    from flask import Flask
    from dotenv import load_dotenv
    import os

    load_dotenv()

    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.environ.get("SECRET_KEY"),
                            UPLOAD_FOLDER=os.environ.get("UPLOAD_FOLDER"),
                            ALLOWED_EXTENSIONS=ALLOWED_EXTENSIONS)

    from .handlers import bp_users
    app.register_blueprint(bp_users)

    return app
