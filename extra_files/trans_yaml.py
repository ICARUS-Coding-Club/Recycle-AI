import yaml
 
with open(rf'C:\Users\hong_\Desktop\YOLOv5\Recycle-AI\Recycle-AI\dataset\trash02\data.yaml', 'r') as f:
	data = yaml.safe_load(f)
 
data['train'] = rf'C:\Users\hong_\Desktop\YOLOv5\Recycle-AI\Recycle-AI\dataset\trash02\train.txt'
data['valid'] = rf'C:\Users\hong_\Desktop\YOLOv5\Recycle-AI\Recycle-AI\dataset\trash02\valid.txt'
 
with open(rf'C:\Users\hong_\Desktop\YOLOv5\Recycle-AI\Recycle-AI\dataset\trash02\data.yaml', 'w') as f:
	yaml.dump(data, f)