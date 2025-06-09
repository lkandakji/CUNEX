# CUNEX
CUNEX is a generalizable segmentation model based on the nnU-Net framework for full corneal segmentation from AS-OCT images, validated on healthy, keratoconus, Fuchs dystrophy and infectious kerititis eyes.

# System Requirements
**Python Dependencies**
```
Package                       Version
----------------------------- -----------
absl-py                       2.3.0
acvl_utils                    0.2.5
asttokens                     3.0.0
astunparse                    1.6.3
batchgenerators               0.25.1
batchgeneratorsv2             0.3.0
blosc2                        3.3.4
certifi                       2025.4.26
charset-normalizer            3.4.2
comm                          0.2.2
connected-components-3d       3.23.0
contourpy                     1.3.2
cycler                        0.12.1
debugpy                       1.8.14
decorator                     5.2.1
dynamic_network_architectures 0.4.1
einops                        0.8.1
exceptiongroup                1.3.0
executing                     2.2.0
fft-conv-pytorch              1.2.0
filelock                      3.18.0
flatbuffers                   25.2.10
fonttools                     4.58.1
fsspec                        2025.5.1
future                        1.0.0
gast                          0.6.0
google-pasta                  0.2.0
graphviz                      0.20.3
grpcio                        1.72.1
h5py                          3.13.0
hf-xet                        1.1.3
huggingface-hub               0.32.4
idna                          3.10
imagecodecs                   2025.3.30
imageio                       2.37.0
imgaug                        0.4.0
importlib_resources           6.5.2
ipykernel                     6.29.5
ipython                       8.37.0
jedi                          0.19.2
Jinja2                        3.1.6
joblib                        1.5.1
jupyter_client                8.6.3
jupyter_core                  5.8.1
keras                         3.10.0
kiwisolver                    1.4.8
lazy_loader                   0.4
libclang                      18.1.1
linecache2                    1.0.0
Markdown                      3.8
markdown-it-py                3.0.0
MarkupSafe                    3.0.2
matplotlib                    3.10.3
matplotlib-inline             0.1.7
mdurl                         0.1.2
ml_dtypes                     0.5.1
mpmath                        1.3.0
msgpack                       1.1.0
namex                         0.1.0
ndindex                       1.10.0
nest-asyncio                  1.6.0
networkx                      3.4.2
nibabel                       5.3.2
nnunetv2                      2.6.2
numexpr                       2.10.2
numpy                         1.23.5
nvidia-cublas-cu12            12.6.4.1
nvidia-cuda-cupti-cu12        12.6.80
nvidia-cuda-nvrtc-cu12        12.6.77
nvidia-cuda-runtime-cu12      12.6.77
nvidia-cudnn-cu12             9.5.1.17
nvidia-cufft-cu12             11.3.0.4
nvidia-cufile-cu12            1.11.1.6
nvidia-curand-cu12            10.3.7.77
nvidia-cusolver-cu12          11.7.1.2
nvidia-cusparse-cu12          12.5.4.2
nvidia-cusparselt-cu12        0.6.3
nvidia-nccl-cu12              2.26.2
nvidia-nvjitlink-cu12         12.6.85
nvidia-nvtx-cu12              12.6.77
opencv-python                 4.11.0.86
opt_einsum                    3.4.0
optree                        0.16.0
packaging                     25.0
pandas                        2.2.3
parso                         0.8.4
pexpect                       4.9.0
pillow                        11.2.1
pip                           25.1
platformdirs                  4.3.8
prompt_toolkit                3.0.51
protobuf                      5.29.5
psutil                        7.0.0
ptyprocess                    0.7.0
pure_eval                     0.2.3
py-cpuinfo                    9.0.0
Pygments                      2.19.1
pyparsing                     3.2.3
python-dateutil               2.9.0.post0
pytz                          2025.2
PyYAML                        6.0.2
pyzmq                         26.4.0
requests                      2.32.3
rich                          14.0.0
safetensors                   0.5.3
scikit-image                  0.25.2
scikit-learn                  1.6.1
scipy                         1.15.3
seaborn                       0.13.2
setuptools                    78.1.1
shapely                       2.1.1
simpleitk                     2.5.0
six                           1.17.0
stack-data                    0.6.3
sympy                         1.14.0
tensorboard                   2.19.0
tensorboard-data-server       0.7.2
tensorflow                    2.19.0
tensorflow-io-gcs-filesystem  0.37.1
termcolor                     3.1.0
threadpoolctl                 3.6.0
tifffile                      2025.5.10
timm                          1.0.15
torch                         2.7.0
torchaudio                    2.7.0
torchvision                   0.22.0
tornado                       6.5.1
tqdm                          4.67.1
traceback2                    1.4.0
traitlets                     5.14.3
triton                        3.3.0
typing_extensions             4.14.0
tzdata                        2025.2
unittest2                     1.1.0
urllib3                       2.4.0
wcwidth                       0.2.13
Werkzeug                      3.1.3
wheel                         0.45.1
wrapt                         1.17.2
yacs                          0.1.8
```
# Environment Variables
CUNEX requires some environment variables so that it always knows where the raw data and trained models are. Depending on the operating system, these environment variables need to be set in different ways. These are instructions for Linux & MacOS:

Locate the ```.bashrc``` file in your home folder and add the following lines to the bottom:
```
export nnUNet_raw="{working_dir}/nnUNet_raw"
export nnUNet_results="{working_dir}/nnUNet_results"
```
Then execute echo ${nnUNet_raw} etc to check that its been done. Or you can simply execute the following lines whenever you run CUNEX in terminal.

# Data Prep
The only way to run inference with CUNEX is by storing it in the nnU-Net format.
1. You must add a directory ```{working_dir}/dataset``` where you will create two subdirectories ```nnunet_trained_model``` and ```nnunet_raw```.
2. In ```/nnunet_trained_model``` you will save the model weights file.
3. In ```/nnunet_raw``` you will make directories for your dataset(s) in the format ```/Dataset0001_{name of dataset}``` like:
```
  nnUNet_raw/
├── Dataset001_BrainTumour
├── Dataset002_Heart
├── Dataset003_Liver
├── Dataset004_Hippocampus
├── Dataset005_Prostate
├── ...
```
5. Preprocess your image dataset directory using ```data_prep.ipynb```. CUNEX expects the same file format for images that it was trained on (png). BMP and WEBP conversion functions are available, but you may easily add a cell for whichever extension conversion is necessary.

# Run
Run inference with ```nnunetv2/inference/inference.py```. Be sure to change paths where specified. The predicted masks are binary, so an addtional directory ```/Dataset0001_imagesTs_pred_vis``` is made with visible masks for your viewing.
