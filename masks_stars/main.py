import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_opening
from skimage.measure import label


s_plus = np.zeros((5, 5))
s_plus[2,:] = 1
s_plus[:,2] = 1
s_cross = np.zeros((5, 5))
for i in range(5):
    s_cross[i,i] = 1
    s_cross[4-i,i] = 1
    

image = np.load('stars.npy')
plusses = label(binary_opening(image, s_plus))
crosses = label(binary_opening(image, s_cross))


counts_pl = list(set(plusses.flatten()))[-1]
counts_cr = list(set(crosses.flatten()))[-1]
print("Кол-во плюсов", counts_pl)
print("Кол-во крестов", counts_cr)
print("Кол-во звёздочек", counts_pl + counts_cr)


image = plusses
for i in range(image.shape[0]):
    for j in range(image.shape[0]):
        if crosses[i,j] != 0:
            image[i,j] = crosses[i,j]
plt.imshow(image)
plt.show()
