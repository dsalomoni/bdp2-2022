import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray

original = io.imread('taipei.jpg')
grayscale = rgb2gray(original)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title('Original')
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].set_title('Grayscale')

fig.tight_layout()
plt.savefig('taipei_bw.pdf')
plt.cla()
plt.close()