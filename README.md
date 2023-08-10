# README

## 참고 사이트
https://minding-deep-learning.tistory.com/19


## 모델 학습 실행 명령어
    python train.py --img 640 --batch 16 --epochs 20 --data ~/dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name yolov5_coco

## 이미지 판별 실행 명령어
모델 이름 설정 (model_name): ex) exp   
판별할 이미지 이름 (image_name): ex) test_image

    python ./yolov5-master/detect.py --weights ./yolov5-master/runs/train/[model_name]/weights/best.pt --img 640 --conf 0.5 --source ./images/[image_name].jpg