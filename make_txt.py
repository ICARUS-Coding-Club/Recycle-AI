from glob import glob
 
# 이미지들의 주소 리스트로 만들어줌
train_img_list = glob(rf'C:\Users\hong_\Desktop\YOLOv5\Microsoft COCO.v2-raw.yolov5pytorch\train\images\*.jpg')
valid_img_list = glob(rf'C:\Users\hong_\Desktop\YOLOv5\Microsoft COCO.v2-raw.yolov5pytorch\valid\images\*.jpg')
 
# 리스트를 txt파일로 생성
with open(rf'./dataset/train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open(rf'./dataset/valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')