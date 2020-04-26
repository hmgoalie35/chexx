from math import floor

import cv2 as cv
from flask import current_app


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class BaseTracker(object):
    def handle_frame(self, frame):
        raise NotImplementedError()


class TensorflowPuckTracker(BaseTracker):
    def __init__(self, *args, **kwargs):
        self.net = cv.dnn.readNetFromTensorflow(
            str(current_app.config['TF_FROZEN_INF_GRAPH_FILE']),
            str(current_app.config['TF_GRAPH_FILE'])
        )
        self.threshold = 0.3

    def handle_frame(self, frame):
        rows, cols, channels = frame.shape
        self.net.setInput(cv.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False))
        net_output = self.net.forward()

        for detection in net_output[0, 0]:
            score = float(detection[2])
            if score < self.threshold:
                continue

            bottom_box_left = int(detection[3] * cols)
            bottom_box_top = int(detection[4] * rows)
            bottom_box_right = int(detection[5] * cols)
            bottom_box_bottom = int(detection[6] * rows)

            box_offset = 25
            top_box_top = bottom_box_top + box_offset

            cv.rectangle(
                img=frame,
                pt1=(bottom_box_left, top_box_top),
                pt2=(bottom_box_right, bottom_box_top),
                color=GREEN,
                thickness=-1
            )
            cv.rectangle(
                img=frame,
                pt1=(bottom_box_left, bottom_box_top),
                pt2=(bottom_box_right, bottom_box_bottom),
                color=GREEN,
                thickness=2
            )
            cv.putText(
                img=frame,
                text=f'{round(score * 100)}%',
                org=(bottom_box_left, bottom_box_top + (floor(box_offset / 2))),
                fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL,
                color=BLACK,
                fontScale=.9,
                lineType=1,
                thickness=1
            )

        return frame


class OpenCVPuckTracker(BaseTracker):
    def __init__(self):
        super().__init__()
        cascade_file = current_app.config['OPENCV_CASCADE_FILE']
        self.cascade = cv.CascadeClassifier(str(cascade_file))
        if self.cascade.empty():
            self.cascade = None
            print(f'Failed to load cascade file {cascade_file}')

    def handle_frame(self, frame):
        if self.cascade is None:
            return frame

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        pucks = self.cascade.detectMultiScale(gray, 20, 20)
        for x, y, w, h in pucks:
            center = (x + w // 2, y + h // 2)
            radius = int(round((w + h) * 0.25))
            frame = cv.circle(frame, center, radius, GREEN, 2)
            # frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, GREEN, 4)
            # frame = cv.rectangle(frame, (x, y), (x + w, y + h), GREEN, 1)
            # cv.putText(
            #     img=frame,
            #     text='puck',
            #     org=(x, y),
            #     fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL,
            #     color=BLACK,
            #     fontScale=.9,
            #     lineType=1,
            #     thickness=1
            # )
        return frame
