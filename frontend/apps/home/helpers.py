from math import floor

import cv2 as cv
from flask import current_app


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class ChexxTracker:
    def __init__(self, *args, **kwargs):
        self.net = cv.dnn.readNetFromTensorflow(
            str(current_app.config['DATA_MODEL_DIR'] / 'frozen_inference_graph.pb'),
            str(current_app.config['DATA_MODEL_DIR'] / 'graph.pbtxt')
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
