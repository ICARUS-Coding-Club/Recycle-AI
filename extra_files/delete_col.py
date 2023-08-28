import os

# 입력 폴더 경로 설정
input_folder = rf"C:\Users\hong_\Desktop\dataset\styrofoam.v3i.yolov5pytorch\train\labels"  # 수정 필요

# 입력 폴더 내의 모든 텍스트 파일을 대상으로 작업 수행
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):  # 확장자가 .txt인 파일만 대상으로
        input_file = os.path.join(input_folder, filename)

        with open(input_file, 'r') as f:
            lines = f.readlines()

        # 공백이 5개 이상인 행을 제외하고 원본 파일에 덮어쓰기
        with open(input_file, 'w') as f:
            for line in lines:
                if line.count(' ') < 5:
                    f.write(line)
