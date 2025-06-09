# CUNEX
CUNEX is a generalizable segmentation model based on the nnU-Net framework for full corneal segmentation from AS-OCT images, validated on healthy, keratoconus, Fuchs dystrophy and infectious kerititis eyes.
# System Requirements

# Data Prep
The only way to run inference with CUNEX is by storing it in the nnU-Net format.
1. You must add a directory ```/dataset``` where you will create two subdirectories ```nnunet_trained_model``` and dataset/nnunet_raw/nnunet_raw_data```.
2. In ```/nnunet_trained_model``` you will save the model weights file.
3. In ```/nnunet_raw_data``` you will make directories for your dataset in the format ```/Dataset0001_{name of dataset}```.
4. Preprocess your image dataset directory ```data_prep.ipynb```. CUNEX expects the same file format for images that it was trained on (png). BMP and WEBP conversion functions are available, but you may easily add a cell for whichever extension conversion is necessary.

# Run
Run interference with ```nnunetv2/inference/inference.py```. Be sure to change paths where specified. The predicted masks are binary, so an addtional directory ```/Dataset0001_imagesTs_pred_vis``` is made with visible masks for your viewing.
