import yaml
 
with open('./dataset/data.yaml', 'r') as f:
	data = yaml.safe_load(f)
 
data['train'] = './dataset/train.txt'
data['valid'] = './dataset/valid.txt'
 
with open('./dataset/data.yaml', 'w') as f:
	yaml.dump(data, f)