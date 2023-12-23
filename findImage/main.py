import cv2

cv2.namedWindow("Video", cv2.WINDOW_KEEPRATIO)
cam = cv2.VideoCapture("output.avi")

image = cv2.imread('rassohin.png', cv2.IMREAD_UNCHANGED)

frame_count = 0
image_count = 0

while cam.isOpened():
    ret, frame = cam.read()

    if not ret:
        break

    _, max_val, _, _ = cv2.minMaxLoc(cv2.matchTemplate(frame, image, cv2.TM_CCOEFF_NORMED))
    
    cv2.imshow("Video", frame)

    if max_val >= 0.8:
        image_count += 1
        print(image_count)
    frame_count += 1
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(f"кол-во всех изображений {frame_count}")
print(f"кол-во моих изображений {image_count}")

cam.release()
cv2.destroyAllWindows()
