import cv2 as cv

from conf import VIDEO_DIR
from trackers.base import BaseTracker


BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
LINE_THICKNESS = 2


class PuckTracker(BaseTracker):
    def handle_frame(self, frame):
        roi = frame[250: 1000, 100: 1600]
        rows, cols, _ = roi.shape

        gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

        gray_roi = cv.GaussianBlur(gray, (7, 7), 0)

        # _, threshold = cv.threshold(gray_roi, 32, 255, cv.THRESH_BINARY_INV)
        # threshold = cv.adaptiveThreshold(gray_roi, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
        threshold = cv.adaptiveThreshold(gray_roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)

        contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # contours = [c for c in contours if cv.isContourConvex(c)]
        contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)

        for cnt in contours:
            (x, y, w, h) = cv.boundingRect(cnt)

            # cv.drawContours(roi, [cnt], 0, BLUE, LINE_THICKNESS)
            cv.rectangle(gray_roi, (x, y), (x + w, y + h), BLUE, LINE_THICKNESS)
            cv.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), GREEN, LINE_THICKNESS)
            cv.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), GREEN, LINE_THICKNESS)
            break

        cv.imshow("threshold", threshold)
        # cv.imshow("gray roi", gray_roi)
        cv.imshow("roi", roi)


if __name__ == '__main__':
    t = PuckTracker(file_name=VIDEO_DIR / '20200408_223521.mp4')
    t.run()
