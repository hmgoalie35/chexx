import cv2
from flask import Response, current_app, render_template, views

from .helpers import ChexxTracker


class HomeView(views.MethodView):
    def get(self, *args, **kwargs):
        return render_template('home.html')


class StreamView(views.MethodView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tracker = ChexxTracker()

    def get_frame(self, camera):
        while True:
            _, frame = camera.read()
            frame = self.tracker.handle_frame(frame)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield (
                b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n'
            )

    def get(self, *args, **kwargs):
        if current_app.camera:
            return Response(
                self.get_frame(current_app.camera),
                mimetype='multipart/x-mixed-replace; boundary=frame'
            )
        else:
            return Response()
