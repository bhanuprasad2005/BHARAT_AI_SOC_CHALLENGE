#Dataset: Brain MRI Images for Brain Tumor Detection

This project uses the Brain MRI Images for Brain Tumor Detection dataset, which is publicly available on Kaggle. It contains a collection of magnetic resonance imaging (MRI) scans of human brains that are labeled based on the presence or absence of tumors. MRI is a widely used non-invasive imaging technique in medical diagnostics that helps detect abnormalities in soft tissues, such as brain tumors, without using ionizing radiation.

# Dataset Structure

The dataset is organized into two main folders:

yes — MRI images where a brain tumor is present

no — MRI images where no tumor is present

Each class folder contains 2D MRI scans in JPEG/PNG format. These images can vary in resolution, typically ranging from small (e.g., roughly 88×88) to larger images (up to ~300×300), and are used to train and evaluate binary classification models for tumor detection.

# Purpose and Use

This dataset is used to:

Train machine learning and deep learning models for tumor detection and classification

Benchmark the performance of CNNs and similar architectures in medical image analysis

Support research in automated brain tumor diagnosis using computer vision techniques

As a binary classification dataset, it provides a realistic scenario for distinguishing between healthy and tumorous brain MRI scans, a crucial task in medical imaging applications.

#The entire  procedure done
Step 1 – Trained model on PC (VS Code)
Using TensorFlow / Keras
Step 2 – Simplifed model
Reduced:
Image size → 64×64 or 96×96
Filter size smaller
Reduced pooling complexity
Step 3 – Extracted weights
Step 4 – Implemented convolution accelerator in FPGA (HLS)
Step 5 – Compared the results
