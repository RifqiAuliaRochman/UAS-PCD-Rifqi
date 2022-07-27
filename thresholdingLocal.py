from skimage import data
import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.color import rgb2gray

gambarasli = data.astronaut()
gambarabu = rgb2gray(gambarasli)
gambar_edge = sobel(gambarabu)

plt.imshow(gambarabu, cmap=plt.cm.gray)
plt.show()
plt.gray()
plt.imshow(gambar_edge)
plt.show()