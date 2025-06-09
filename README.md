# CUNEX
CUNEX is a generalizable segmentation model based on the nnU-Net framework for full corneal segmentation from AS-OCT images, validated on healthy, keratoconus, Fuchs dystrophy and infectious keratitis eyes.

# 👁️ Quickstart
1. Clone this repo
2. Create a venv and install 'requirements.txt'
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
3. In ```/nnunet_raw``` you will make directories for your dataset(s) in the format ```/Dataset0001_{name of dataset}```. Your directory set up should look like this:
```
{working_dir}/
├── nnunet_trained_model/
│   └── cunex.pth
├── nnunet_raw/
│   └── Dataset001_Glioblastoma/
│       ├── imagesTs/
│       ├── imagesTr/
│       └── labelsTr/
│   └── Dataset001_Glaucoma/
│   └── ...
```

5. Preprocess your image dataset directory using the ```data_prep.ipynb``` notebook. The model expects the same file format for images that it was trained on (png). Conversion functions for BMP and WEBP are already included, and you can easily add a new cell to handle other file formats if needed.

# Run
Run inference with ```nnunetv2/inference/inference.py```. Be sure to change paths where specified. The predicted masks are binary, so an additional directory ```/Dataset0001_imagesTs_pred_vis``` is made with visible masks for your viewing.
