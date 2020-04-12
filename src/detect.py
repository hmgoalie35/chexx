import cv2 as cv

from conf import DATA_IMG_DIR, DATA_MODEL_DIR


def detect():
    cvNet = cv.dnn.readNetFromTensorflow(
        str(DATA_MODEL_DIR / 'frozen_inference_graph.pb'),
        str(DATA_MODEL_DIR / 'graph.pbtxt')
    )

    img = cv.imread(str(DATA_IMG_DIR / 'puck8.jpg'))
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet.forward()

    for detection in cvOut[0, 0, :, :]:
        score = float(detection[2])
        if score > 0.3:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

    cv.imshow('img', img)
    cv.waitKey()
