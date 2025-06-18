# CUNEX
CUNEX is a generalizable segmentation model based on the nnU-Net framework for full corneal segmentation from AS-OCT images, validated on healthy, keratoconus, Fuchs dystrophy and infectious keratitis eyes.

# 👁️ Quickstart
1. Clone this repo
2. Create a venv and install `requirements.txt`
3. Download model weights and save in `nnunet_trained_model/`
4. Set environment variables
5. Format your dataset under `nnUNet_raw/`
6. Preprocess with `data_prep.ipynb`
7. Run inference using `inference.py`

# System Requirements
Install python dependencies via:
```
pip install -r requirements.txt
```
It's recommended to do this inside a virtual environment (e.g., venv or conda) to avoid conflicts with system packages.

# Environment Variables
CUNEX requires some environment variables so that it always knows where the raw data and trained models are. They only need to be set once. These are instructions for Linux & MacOS:

Locate the ```.bashrc``` file in your home folder and add the following lines to the bottom:
```
export nnUNet_raw="{working_dir}/nnUNet_raw"
export nnUNet_results="{working_dir}/nnunet_trained_model"
```
Then execute echo ${nnUNet_raw} etc to check the path is correct. Or you can simply execute the following lines whenever you run CUNEX in a new terminal.

# Model Weights
The CUNEX trained model weights file can be downloaded from the release here https://github.com/lkandakji/CUNEX/releases/download/v1.0/cunex.pth.

# Preparing your data
The only way to run inference with CUNEX is by storing it in the nnU-Net format.
1. You must create two directories ```nnunet_trained_model``` and ```nnunet_raw```.
2. In ```/nnunet_trained_model``` you will save the model weights file ```cunex.pth```.
3. In ```/nnunet_raw``` you will make directories for your dataset(s) in the format ```/Dataset0001_{name of dataset}```. You can create the ```imagesTs``` subdirectories yourself or let the code create them during inference. Your directory will look like this:
```
{working_dir}/
├── nnunet_trained_model/
│   └── cunex.pth
├── nnunet_raw/
│   └── Dataset001_Keratoconus/
│       ├── imagesTs/
│       ├── imagesTs_pred/
│       └── imagesTs_pred_vis/
│   └── Dataset001_FECD/
│   └── ...
```

5. Preprocess your image dataset directory using the ```data_prep.ipynb``` notebook. The model expects the same file format for images that it was trained on (png). Conversion functions for BMP and WEBP are already included, and you can easily add a new cell to handle other file formats if needed.

# Run
Run inference with ```nnunetv2/inference/inference.py```. Be sure to change paths where specified. The predicted masks are binary, so an additional directory ```/Dataset0001_imagesTs_pred_vis``` is made with visible masks for your viewing.

# External Validation
An AS-OCT image dataset for segmentation is made available here: https://springernature.figshare.com/collections/AIDK_An_AS-OCT_image_dataset_for_deep_learning-enabled_segmentation_and_3D_reconstruction_for_keratitis/7036994/1
It contains a total of 1168 AS-OCT images of patients with keratitis, including 768 full-frame images (6 patients). Each image has associated segmentation labels for lesions and cornea, and also labels of iris for full-frame images.
Citation: Ye, Juan (2024). AIDK: An AS-OCT image dataset for deep learning-enabled segmentation and 3D reconstruction for keratitis. figshare. Collection. https://doi.org/10.6084/m9.figshare.c.7036994.v1

Although our data is not available publically, you may get in contact with me at smgxlk0@ucl.ac.uk to discuss potential collaborations.
