import cv2
from skimage.measure import label, regionprops

image = cv2.imread('balls_and_rects.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:, :, 0]

binary = image.mean(2) > 0
labeled = label(binary)
regions = regionprops(labeled)

circ = 0
circ_clr = []
rect = 0
rect_clr = []

for region in regions:
  r = hsv[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
  if r[0][0] != 0:
    rect += 1
    rect_clr.append(r[0][0])
  else:
    circ += 1
    circ_clr.append(r[0][len(r[0]) // 2])

print(f"Кол-во фигур: {circ + rect}")
print(f"Кол-во цветов фигур: {len(set(circ_clr + rect_clr))}")
print(f"Кол-во кругов: {circ}")
print(f"Кол-во цветов кругов: {len(set(circ_clr))}")
print(f"Кол-во прямоугольников: {rect}")
print(f"Кол-во цветов прямоугольников: {len(set(rect_clr))}")
