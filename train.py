import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import RTDETR



if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/MCL-DETR.yaml')
    model.train(data='/home/Exp_paper/RTDETR-main/dataset/luna16/data.yaml',
                cache=False,
                imgsz=640,
                epochs=150,
                batch=8,
                workers=4, #
                name='luna16',
                )