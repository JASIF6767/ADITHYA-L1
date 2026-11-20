from astropy.io import fits
import matplotlib.pyplot as plt

filename = r"C:\Users\JASIF\OneDrive\Desktop\python\PART A\NB04.fits"
hdul = fits.open(filename)
print(hdul.info())
data = hdul[0].data

print("Shape =", data.shape)
print("Min =", data.min())
print("Max =", data.max())
print("Mean =", data.mean())
import matplotlib.pyplot as plt

plt.hist(data.flatten(), bins=100)
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.title("Histogram of Pixel Intensities")
plt.show()
from skimage.filters import threshold_otsu

threshold = threshold_otsu(data)

print("Threshold =", threshold)

mask = data > threshold

plt.imshow(mask, cmap='gray')
plt.title("Binary Mask")
plt.show()