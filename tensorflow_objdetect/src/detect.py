import cv2 as cv

from conf import DATA_IMG_DIR, DATA_MODEL_DIR


def detect():
    # Load a model imported from Tensorflow
    tensorflowNet = cv.dnn.readNetFromTensorflow(
        str(DATA_MODEL_DIR / 'frozen_inference_graph.pb'),
        str(DATA_MODEL_DIR / 'graph.pbtxt')
    )

    # Input image
    img = cv.imread(str(DATA_IMG_DIR / 'puck82.jpg'))
    rows, cols, channels = img.shape

    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()

    # Loop on the outputs
    for detection in networkOutput[0, 0]:

        score = float(detection[2])
        if score > 0.3:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows

            cv.rectangle(img, (int(left), int(top + 25)), (int(right), int(top)), (0, 255, 0), thickness=-1)
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), thickness=2)

            cv.putText(
                img=img,
                text=f'{round(score * 100)}%',
                org=(int(left), int(top + 12)),
                fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL,
                color=(0, 0, 0),
                fontScale=.9,
                lineType=1,
                thickness=1
            )

    # Show the image with a rectagle surrounding the detected objects
    winname = 'image'
    cv.namedWindow(winname, cv.WINDOW_NORMAL)
    cv.resizeWindow(winname, width=cols, height=rows)
    cv.imshow(winname, img)

    if cv.waitKey() == 27:
        cv.destroyAllWindows()
