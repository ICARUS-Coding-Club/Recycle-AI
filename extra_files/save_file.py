import os
import shutil
import glob

# 폴더 경로 설정
folder_path = rf"C:\Users\hong_\Desktop\YOLOv5\recycle_dataset\train\labels"  # 폴더 경로를 적절히 변경하세요
invalid_filenames = []

# 폴더 내의 모든 파일 가져오기
file_paths = glob.glob(os.path.join(folder_path, "*.txt"))

# 각 파일에 대한 검사
for file_path in file_paths:
    filename = os.path.basename(file_path)
    first_character = filename[0]
    
    if first_character in ('0'):
        # 첫 글자가 0 또는 1이 아닌 파일명을 리스트에 추가
        invalid_filenames.append(filename)

print(invalid_filenames)

# 파일명 리스트와 파일들이 들어있는 폴더 경로 설정
file_names_to_move = invalid_filenames  # 이동할 파일명들
source_folder_path = rf"C:\Users\hong_\Desktop\YOLOv5\recycle_dataset\train\labels"  # 파일들이 들어있는 폴더 경로
destination_folder_path = rf"C:\Users\hong_\Desktop\YOLOv5\recycle_dataset\train01\labels"  # 파일을 이동할 대상 폴더 경로

# 대상 폴더가 없으면 생성
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

# 파일명 리스트에 있는 파일들을 대상 폴더로 이동
for file_name in file_names_to_move:
    source_file_path = os.path.join(source_folder_path, file_name)
    destination_file_path = os.path.join(destination_folder_path, file_name)
    
    if os.path.exists(source_file_path):
        try:
            shutil.move(source_file_path, destination_file_path)
            print(f"파일 {file_name}을 {destination_folder_path}로 이동했습니다.")
        except Exception as e:
            print(f"파일 {file_name}을 이동하는 도중 오류가 발생했습니다: {str(e)}")
    else:
        print(f"파일 {file_name}은 {source_folder_path}에 존재하지 않습니다.")