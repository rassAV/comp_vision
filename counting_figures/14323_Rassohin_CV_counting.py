import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import binary_opening
from skimage.measure import label



rects = [np.ones((4, 6)), np.ones((6, 4))]
bitten_rects = [np.ones((4, 6)), np.ones((4, 6)), np.ones((6, 4)), np.ones((6, 4))]
bitten_rects[0][2:4,2:4] = 0
bitten_rects[1][0:2,2:4] = 0
bitten_rects[2][2:4,0:2] = 0
bitten_rects[3][2:4,2:4] = 0



image = np.load("ps.npy.txt")



summR = 0
for i, r in enumerate(rects):
    res = label(binary_opening(image, r))
    counts = list(set(res.flatten()))[-1]
    summR += counts
    print("Кол-во прямоугольников("+str(i)+"):", counts)
print("Общее кол-во прямоугольников:", summR, "\n")



summBR = 0
for i, b_r in enumerate(bitten_rects):
    res = label(binary_opening(image, b_r))
    counts = list(set(res.flatten()))[-1]
    summBR += counts
    print("Кол-во откусанных прямоугольников("+str(i)+"):", counts)
print("Общее кол-во откусанных прямоугольников:", summBR)

print("\nКол-во всех фигур:", summR + summBR)



plt.imshow(image)
plt.show()
