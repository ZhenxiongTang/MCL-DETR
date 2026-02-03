# UL-DETR

## Abstract


## 📋 Publication Status
**Current Status:** Manuscript under peer review  

**Code Availability:** The source code is available at here


## 📊 Experimental Datasets

### DeepLesion Dataset
- **Source:** https://nihcc.box.com/v/DeepLesion
- **Usage:** Universal Lesion detection 
### Lung-PET-CT-Dx Dataset  
- **Source:** https://www.cancerimagingarchive.net/collection/lung-pet-ct-dx/
- **Usage:** Lung cancer Lesion detection 

## 🔄 Updates
- **[Future]:** Code has been uploaded and is available


# 🚀Quick start 
## 1. 🛠️Setup
```bash
conda create -n mcl python==3.10
conda activate mcl
pip install -r requirements.txt            
```

## 2. 📚Data Preparation

### DeepLesion Dataset
- **Source:** https://nihcc.box.com/v/DeepLesion
- **Usage:** Universal Lesion detection 
### Lung-PET-CT-Dx Dataset  
- **Source:** https://www.cancerimagingarchive.net/collection/lung-pet-ct-dx/
- **Usage:** Lung cancer Lesion detection


### 2.1 🔧Custom Dataset
<details>
<summary> <b>Structure your dataset directories as follows: </b> </summary>
    
```
dataset/
├── images/
│   ├── train/          
│   ├── val/
│   └── test/    
└── labels/
│   ├── train/          
│   ├── val/
│   └── test/
└── data.yaml      
```   

</details>  

### 2.2 🔄Update Configuration Files:

Modify your data.yml.
```shell
# dataset path
path: /home/Exp_paper/RTDETR-main/dataset/
train: ./luna16/images/train
val: ./luna16/images/val
test: ./luna16/images/test

# number of classes
nc: 1

# class names
names:
  0: Lungnodule
```

## 3.🚂Training
```shell
python train.py
```

## 4.🎲Testing
```shell
python val.py
```
## 🤝Acknowledgement 
Our work is built upon RT-DETR and ultralytics. Thanks to the inspirations from RT-DETR.

