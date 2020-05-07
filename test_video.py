import cv2 as cv

cap = cv.VideoCapture(0)

while True:
   ret, frame = cap.read()
   if not ret:
       break
   cv.imshow('test', frame)
   if cv.waitKey(1) == 27:
       cv.destroyAllWindows()
       break

