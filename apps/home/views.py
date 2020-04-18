from flask import views, render_template, Response, current_app
from helpers import ChexxTracker
import cv2

class HomeView(views.MethodView):
    def get(self, *args, **kwargs):
        return render_template('home.html')

class StreamView(views.MethodView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tracker = ChexxTracker()

    def get_frame(self, camera):
        while True:
            #get camera frame
            _, frame = camera.read()
            frame = self.tracker.handle_frame(frame)
            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    def get(self, *args, **kwargs):
        if current_app.camera:
            return Response(self.get_frame(current_app.camera),
                            mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            return Response()
