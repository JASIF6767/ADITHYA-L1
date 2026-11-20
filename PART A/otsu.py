"""
Aditya-L1 SUIT Data Analysis: Active Region Detection
Description: Isolates extreme ultraviolet emissions using Otsu's thresholding 
and morphological operations to draw contours around solar flares.
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage.morphology import opening, disk

# 1. Open the file and load the L1 data
filename = r"C:\Users\JASIF\OneDrive\Desktop\python\PART A\NB04.fits"
with fits.open(filename) as hdul:
    data = hdul[0].data

# 2. Process the image (Thresholding + Morphological Opening)
threshold = threshold_otsu(data)
mask = data > threshold
cleaned_mask = opening(mask, disk(3))

# 3. Generate the Final Visualization
fig, ax = plt.subplots(figsize=(8, 8))

# Draw the thermal false-color background
ax.imshow(data, cmap='afmhot', vmin=4000, vmax=15000)

# Draw the cyan boundary contour over the flare footprints
ax.contour(cleaned_mask, levels=[0.5], colors='cyan', linewidths=2)

# Format the presentation
ax.set_title("Aditya-L1 SUIT: X6.3 Flare Active Regions (Feb 22, 2024)")
ax.axis('off') 

# Display the final result
plt.tight_layout()
plt.show()