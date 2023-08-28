import os
import glob

# 텍스트 파일이 있는 폴더 경로 지정
folder_path = rf'C:\Users\hong_\Desktop\tubeSkin_labeling.v2i.yolov5pytorch\valid\labels'  # 실제 폴더 경로로 변경해야 합니다.

# 폴더 내의 모든 텍스트 파일을 찾음
file_pattern = os.path.join(folder_path, '*.txt')
file_list = glob.glob(file_pattern)

# 각 파일을 순회하면서 변경 작업 수행
for file_path in file_list:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            parts = line.strip().split()  # 각 줄을 공백으로 나눔
            if parts:  # 줄이 비어있지 않은 경우에만 처리
                if parts[0] == '2':  # 첫 번째 숫자가 0인 경우
                    parts[0] = '12'  # 첫 번째 숫자를 1으로 변경
                new_line = ' '.join(parts) + '\n'
                file.write(new_line)

    print(f"{file_path} 파일의 첫 번째 숫자가 변경되었습니다.")
