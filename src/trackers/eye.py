import cv2

from conf import VIDEO_DIR
from trackers.base import BaseTracker


BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
LINE_THICKNESS = 2


class EyeTracker(BaseTracker):
    def handle_frame(self, frame):
        roi = frame[200: 600, 950: 1200]
        rows, cols, _ = roi.shape
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
        _, threshold = cv2.threshold(gray_roi, 16, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            # cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), BLUE, 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), GREEN, LINE_THICKNESS)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), GREEN, LINE_THICKNESS)
            break

        cv2.imshow("threshold", threshold)
        cv2.imshow("gray roi", gray_roi)
        cv2.imshow("roi", roi)


if __name__ == '__main__':
    t = EyeTracker(file_name=VIDEO_DIR / 'eye.mp4')
    t.run()
