from skimage.filters import try_all_threshold
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

gambarasli = data.astronaut()
gambarabu = rgb2gray(gambarasli)
plt.imshow(gambarasli)
plt.show()

fig, ax = try_all_threshold(
    gambarabu, figsize=(10, 8), verbose=False
)

fig.tight_layout()
plt.show()