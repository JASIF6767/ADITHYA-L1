import os
import glob
import sunpy.map
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops  
import matplotlib.dates as mdates

def load_and_verify_data():
    # 1. Define the exact Windows path
    data_directory = r'C:\Users\JASIF\OneDrive\Desktop\python\PART B'
    
    file_pattern = os.path.join(data_directory, '*.fits')
    file_list = sorted(glob.glob(file_pattern))
    
    if len(file_list) == 0:
        print(f"Error: No FITS files found in '{data_directory}'.")
        return

    # Arrays to store our data for the final graph
    dates = []
    active_region_areas = []
    
    # Variables to remember our tracked region's properties from yesterday
    target_centroid = None
    previous_area = None

    print(f"Starting time-series analysis on {len(file_list)} images...\n")

    # --- STAGE 4: THE TIME-SERIES LOOP ---
    for file_path in file_list:
        print(f"Processing {os.path.basename(file_path)}...")
        
        # Load the map for this specific day
        smap = sunpy.map.Map(file_path)
        data = smap.data
        data_clean = np.nan_to_num(data)
        
        # Two-Step Otsu Segmentation
        space_vs_sun_thresh = threshold_otsu(data_clean)
        sun_mask = data_clean > space_vs_sun_thresh
        pixels_on_sun = data_clean[sun_mask]
        
        active_region_thresh = threshold_otsu(pixels_on_sun)
        binary_mask = (data_clean > active_region_thresh) & sun_mask
        
        # Region Labeling
        labeled_image = label(binary_mask)
        regions = regionprops(labeled_image)
        
        # Filter out noise and solar limb artifacts using the Goldilocks filter
        valid_regions = [r for r in regions if 500 <= r.area <= 100000]
        
        if valid_regions:
            if target_centroid is None:
                # DAY 1: Pick the largest region to start tracking
                target_region = max(valid_regions, key=lambda r: r.area)
                target_centroid = target_region.centroid
                previous_area = target_region.area
                
                print(f"  -> Day 1: Locked onto Target Region. Area: {previous_area}")
            else:
                # DAY 2+: The NEW Similarity Score Formula
                def similarity_score(r):
                    # 1. How far did it move? (Rotation distance)
                    dist = np.sqrt((r.centroid[0] - target_centroid[0])**2 + (r.centroid[1] - target_centroid[1])**2)
                    
                    # 2. Size Ratio (Creates a multiplier >= 1)
                    size_ratio = max(r.area, previous_area) / max(min(r.area, previous_area), 1)
                    
                    # 3. ADD them instead of multiplying, and heavily weight the size ratio!
                    # This prevents distance=0 (static noise) from wiping out the size penalty.
                    return dist + (size_ratio * 100)
                
                # Pick the region with the lowest (best) similarity score
                target_region = min(valid_regions, key=similarity_score)
                
                # Update the position and size for tomorrow
                target_centroid = target_region.centroid 
                previous_area = target_region.area
                
                print(f"  -> Tracked Target Region. Area: {previous_area}")
                
            dates.append(smap.date.datetime)
            active_region_areas.append(previous_area)

    # --- FINAL STAGE: PLOTTING THE GROWTH/DECAY GRAPH ---
    print("\nDrawing the Growth/Decay Graph...")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot the line graph
    ax.plot(dates, active_region_areas, marker='o', linestyle='-', color='red', linewidth=2, markersize=8)
    
    # Make it look professional for your report
    ax.set_title("Temporal Evolution of Target Active Region Area", fontsize=16, fontweight='bold')
    ax.set_xlabel("Observation Date (June 2026)", fontsize=12)
    ax.set_ylabel("Region Area (Total Pixels)", fontsize=12)
    
    # Format the dates on the bottom axis nicely
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    load_and_verify_data()