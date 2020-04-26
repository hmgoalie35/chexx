import cv2
from flask import Flask

from . import settings
from .urls import blueprints, urlpatterns


def create_app(**config):
    app = Flask(
        __name__,
        static_folder=settings.STATIC_FOLDER,
        static_url_path=settings.STATIC_URL,
        template_folder=settings.TEMPLATE_FOLDER,
    )
    app.config.from_object(settings)
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


application = create_app()
