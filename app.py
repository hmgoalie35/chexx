from flask import Flask

from settings.default import STATIC_FOLDER, STATIC_URL, TEMPLATE_FOLDER
from urls import urlpatterns, blueprints
import cv2

def create_app(**config):
    app = Flask(
        __name__,
        static_folder=STATIC_FOLDER,
        static_url_path=STATIC_URL,
        template_folder=TEMPLATE_FOLDER,
    )
    app.config.from_object('settings.default')
    app.config.update(config)

    # Register any urls, blueprints
    for path, kwargs in urlpatterns:
        app.add_url_rule(path, **kwargs)

    for bp in blueprints:
        app.register_blueprint(bp)

    app.camera = cv2.VideoCapture(0)
    if not app.camera.isOpened():
        print('Unable to open camera')
        app.camera = None

    return app

# Running the app:
# 1. DEV: `export FLASK_DEBUG=1 export FLASK_APP=app.py flask run` or simply `./runserver.sh` for convenience.
# 2. PROD: `gunicorn -w 4 -b 0.0.0.0:4000 app`. Gunicorn automatically looks for a callable named application
# in the specified module.
application = create_app()

# Uncomment this to run this project via `python app.py`.
# if __name__ == '__main__':
#     application.run()

