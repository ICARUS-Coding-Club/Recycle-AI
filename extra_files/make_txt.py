from glob import glob
 
# 이미지들의 주소 리스트로 만들어줌
train_img_list = glob(rf'C:\Users\hong_\Desktop\YOLOv5\trash_test\train\images\*.jpg')
valid_img_list = glob(rf'C:\Users\hong_\Desktop\YOLOv5\trash_test\valid\images\*.jpg')
 
# 리스트를 txt파일로 생성
with open(rf'C:\Users\hong_\Desktop\YOLOv5\Recycle-AI\Recycle-AI\dataset\trash02\train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open(rf'C:\Users\hong_\Desktop\YOLOv5\Recycle-AI\Recycle-AI\dataset\trash02\valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')