from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np 

filename = r"C:\Users\JASIF\OneDrive\Desktop\python\PART A\first.fits"
hdul = fits.open(filename)
image_data = hdul[0].data


vmin = np.percentile(image_data, 1)  
vmax = np.percentile(image_data, 99) 


plt.imshow(image_data, cmap='gray', vmin=vmin, vmax=vmax)
plt.colorbar()
plt.title("My First FITS Image (Contrast Enhanced)")
plt.show()

hdul.close()