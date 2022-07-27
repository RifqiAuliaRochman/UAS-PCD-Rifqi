from scipy import misc
import matplotlib.pyplot as plt
from skimage.filters import gaussian

foto = misc.face()

plt.gray()
plt.imshow(foto)
plt.show()
smoothed = gaussian(foto, multichannel=True, sigma=2)

plt.imshow(smoothed)
plt.show()