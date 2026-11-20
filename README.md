# Aditya-L1 SUIT Data Analysis & Active Region Tracking

This repository contains image processing, feature extraction, and time-series tracking algorithms developed for solar observation data from the **Solar Ultraviolet Imaging Telescope (SUIT)** onboard the **Aditya-L1** mission.

---

## 📌 Project Overview

The project is structured into three main modules focused on the analysis of solar FITS (Flexible Image Transport System) data:

1. **Part A — FITS Image Inspection & Active Region Detection**
   - FITS data ingestion and statistical summary using `astropy.io.fits`.
   - Contrast enhancement with percentile clipping.
   - Intensity histogram distribution analysis.
   - Solar flare / active region detection using Otsu's thresholding and morphological opening operations (`scikit-image`).
   - Generation of solar activity animations.

2. **Part B — Multi-Day Active Region Tracking & Segmentation Comparison**
   - **Time-Series Tracking**: Automated tracking of solar active regions across observation dates, monitoring area evolution and centroid drift driven by solar differential rotation.
   - **Algorithm Comparison**: Evaluation of thresholding algorithms (**Otsu**, **Li**, and **Yen**) on solar disk data to benchmark active region boundary extraction.
   - Output plots, tracking overlays, and time-series trend analysis.

3. **Part C — Reports & Comprehensive Analysis**
   - Detailed documentation and scientific reports summarizing findings, segmentation accuracy, and physical interpretation of the solar features.

---

## 📁 Repository Structure

```text
├── PART A/
│   ├── HISTOGRAM.py              # Pixel intensity histogram generator
│   ├── otsu.py                   # Otsu thresholding & morphological filtering
│   ├── VIEW.py                   # FITS viewer with contrast adjustment
│   ├── animation.py              # Solar time-lapse animation builder
│   ├── animation.gif             # Rendered solar observation animation
│   ├── REPORT.pdf                # Part A analysis report
│   └── OUT PUT/                  # Output plots (Histogram, Otsu segmentation, View)
│
├── PART B/
│   ├── 1finale.py                # Time-series active region tracking pipeline
│   ├── partc.py                  # Comparative evaluation (Otsu vs. Li vs. Yen)
│   ├── Figure_1.png              # Tracking & area evolution curves
│   ├── part c.png                # Segmentation algorithm comparison output
│   ├── 1finale.png               # Final tracking summary visualization
│   ├── report.pdf                # Part B analysis report
│   └── Tracking_Results/         # Daily segmented and tracked solar disk images
│
├── PART C/
│   └── REPORT.pdf                # Part C comprehensive report
│
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements & Dependencies

To run the analysis scripts, ensure you have Python 3.8+ installed along with the following packages:

```bash
pip install numpy matplotlib astropy sunpy scikit-image
```

---

## 🚀 Usage

### 1. Visualizing FITS Data & Intensity Distributions (Part A)
```bash
python "PART A/VIEW.py"
python "PART A/HISTOGRAM.py"
python "PART A/otsu.py"
```

### 2. Time-Series Tracking & Segmentation Comparison (Part B)
```bash
python "PART B/1finale.py"
python "PART B/partc.py"
```

> **Note:** Update the data directory paths in the scripts to point to your local directory containing the `.fits` data files.

---

## 📊 Sample Results

- **Active Region Segmentation:** Automatic isolation of bright UV features from the quieter solar disk.
- **Solar Rotation & Area Drift:** Multi-day centroid tracking documenting active region evolution.
- **Algorithm Evaluation:** Comparison highlighting sensitivity trade-offs between Otsu, Li, and Yen thresholding methods.
