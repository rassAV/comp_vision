import cv2
import numpy as np
import zmq
from skimage.measure import label, regionprops

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://192.168.0.105:6556")

cv2.namedWindow("Camera")
cv2.namedWindow("Mask", cv2.WINDOW_KEEPRATIO)

while True:
    buffer = socket.recv()
    arr = np.frombuffer(buffer, np.uint8)
    frame = cv2.imdecode(arr, -1)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    _, mask = cv2.threshold(hsv[:,:,1], 85, 180, cv2.THRESH_BINARY)
    mask = cv2.dilate(mask, None, iterations=8)

    labeled = label(mask)
    regions = regionprops(labeled)
    
    circles = 0
    squares = 0

    for region in regions:
        y, x = map(int, region.centroid)
        
        coords = region.coords.T
        moments = cv2.moments(region.coords)
        if moments["m00"] != 0:
            circularity = 4 * np.pi * region.area / (region.perimeter ** 2)
            if circularity > 0.9:
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
                circles += 1
            else:
                squares += 1
    
    cv2.putText(frame, f"F{labeled.max()} C{circles} S{squares}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Camera", frame)
    cv2.imshow("Mask", mask)
    
    key = cv2.waitKey(500)
    if key == ord("q"):
        break
