import cv2 as cv

from conf import DATA_IMG_DIR, DATA_MODEL_DIR


def detect():
    # Jean Vitor de Paulo Blog - https://jeanvitor.com/tensorflow-object-detecion-opencv/

    # Load a model imported from Tensorflow
    tensorflowNet = cv.dnn.readNetFromTensorflow(str( DATA_MODEL_DIR / 'frozen_inference_graph.pb' ), str( DATA_MODEL_DIR / 'graph.pbtxt' ))

    # Input image
    img = cv.imread(str(DATA_IMG_DIR / 'puck50.jpg'))
    rows, cols, channels = img.shape

    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()

    # Loop on the outputs
    for detection in networkOutput[0,0]:

        score = float(detection[2])
        if score > 0.2:

            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows

            #draw a red rectangle around detected objects
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)

    # Show the image with a rectagle surrounding the detected objects
    cv.imshow('Image', img)
    cv.waitKey()
    cv.destroyAllWindows()
