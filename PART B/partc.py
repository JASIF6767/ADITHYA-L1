import os
import glob
import sunpy.map
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu, threshold_li, threshold_yen

def compare_segmentation_methods():
    # 1. Define the exact Windows path
    data_directory = r'C:\Users\JASIF\OneDrive\Desktop\python\PART B'
    
    file_pattern = os.path.join(data_directory, '*.fits')
    file_list = sorted(glob.glob(file_pattern))
    
    if len(file_list) == 0:
        print(f"Error: No FITS files found in '{data_directory}'.")
        return

    # 2. We only need ONE image for this comparison
    file_path = file_list[0]
    print(f"Loading {os.path.basename(file_path)} for Part C comparison...")
    
    smap = sunpy.map.Map(file_path)
    data = smap.data
    data_clean = np.nan_to_num(data)
    
    # Step 1: Isolate the Sun from empty space (We use Otsu just to get the sun disk)
    space_vs_sun_thresh = threshold_otsu(data_clean)
    sun_mask = data_clean > space_vs_sun_thresh
    pixels_on_sun = data_clean[sun_mask]
    
    print("\nApplying 3 different segmentation algorithms...")
    
    # --- METHOD 1: OTSU ---
    thresh_otsu = threshold_otsu(pixels_on_sun)
    mask_otsu = (data_clean > thresh_otsu) & sun_mask
    
    # --- METHOD 2: LI ---
    thresh_li = threshold_li(pixels_on_sun)
    mask_li = (data_clean > thresh_li) & sun_mask
    
    # --- METHOD 3: YEN ---
    thresh_yen = threshold_yen(pixels_on_sun)
    mask_yen = (data_clean > thresh_yen) & sun_mask
    
    print(f"Calculated Threshold Values -> Otsu: {thresh_otsu:.2f}, Li: {thresh_li:.2f}, Yen: {thresh_yen:.2f}")

    # --- PLOTTING THE COMPARISON ---
    print("Drawing the side-by-side comparison plot...")
    fig = plt.figure(figsize=(18, 6))
    
    # Plot 1: Original Image
    ax1 = fig.add_subplot(141, projection=smap)
    smap.plot(axes=ax1)
    smap.draw_limb(axes=ax1)
    ax1.set_title('Original Aditya-L1 Image')
    
    # Plot 2: Otsu Mask
    ax2 = fig.add_subplot(142)
    ax2.imshow(mask_otsu, cmap='gray', origin='lower')
    ax2.set_title(f'Method 1: Otsu\n(Thresh: {thresh_otsu:.0f})')
    ax2.axis('off') # Turn off coordinate axes for cleaner look
    
    # Plot 3: Li Mask
    ax3 = fig.add_subplot(143)
    ax3.imshow(mask_li, cmap='gray', origin='lower')
    ax3.set_title(f'Method 2: Li\n(Thresh: {thresh_li:.0f})')
    ax3.axis('off')
    
    # Plot 4: Yen Mask
    ax4 = fig.add_subplot(144)
    ax4.imshow(mask_yen, cmap='gray', origin='lower')
    ax4.set_title(f'Method 3: Yen\n(Thresh: {thresh_yen:.0f})')
    ax4.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_segmentation_methods()