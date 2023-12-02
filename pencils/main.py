import cv2

for num in range(1, 13):
    image = cv2.imread(f"images/img ({num}).jpg")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    pencil_contours = [contour for contour in contours if 250000 < cv2.contourArea(contour) < 400000]
    
    print(f"Pencils count in img {num} - {len(pencil_contours)}")
print("end")
