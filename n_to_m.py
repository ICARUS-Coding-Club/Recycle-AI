import os

# 폴더 경로
folder_path = rf"C:\Users\hong_\Desktop\tubeSkin_labeling.v1i.yolov5pytorch\valid\labels"  # 여러 파일이 포함된 폴더의 경로를 지정하세요.

# 폴더 내의 모든 파일에 대해 작업 수행
for filename in os.listdir(folder_path):
    # 파일의 확장자가 .txt인 경우에만 작업 수행
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # 파일 열기
        with open(file_path, "r") as file:
            # 임시 파일 생성
            temp_file_path = os.path.join(folder_path, "temp.txt")
            
            # 새 파일 열기
            with open(temp_file_path, "w") as new_file:
                # 각 줄을 읽어와 처리
                for line in file:
                    # 각 줄을 공백으로 분리하여 숫자 리스트로 변환
                    numbers = line.split()
                    
                    # 첫 번째 숫자를 0으로 대체
                    numbers[0] = "11"
                    
                    # 수정된 숫자 리스트를 다시 문자열로 변환하여 새 파일에 쓰기
                    new_line = " ".join(numbers)
                    new_file.write(new_line + "\n")
        
        # 임시 파일을 원본 파일로 대체
        os.remove(file_path)
        os.rename(temp_file_path, file_path)

print("작업이 완료되었습니다.")
