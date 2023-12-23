import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)

glass = cv2.imread('deal_with_it.png')
_, glass = cv2.threshold(glass, 50, 255, cv2.THRESH_BINARY)
cascade = cv2.CascadeClassifier(r"haarcascade_eye.xml")

while cam.isOpened():
    ret, frame = cam.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray)
    if len(eyes) == 2:
        x, y, w, h = eyes[0]
        mask = np.zeros((frame.shape[0], frame.shape[1], 3), dtype="uint8")
        mask[:, :, :] = 255
        mask[y:y+glass.shape[0], x-20:x+glass.shape[1]-20] = glass
        
        indices = np.where(mask[:, :, 0] == 255)
        mask[indices] = frame[indices]

        cv2.imshow("Camera", mask)
    else:
        cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
