import os

folder_path = rf'C:\Users\hong_\Desktop\tubeSkin_labeling.v1i.yolov5pytorch\valid\labels'  # 폴더 경로를 여기에 입력하세요.

empty_files = []

# 폴더 내의 모든 파일 목록을 가져옵니다.
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # 파일이 텍스트 파일인지 확인합니다.
    if filename.endswith('.txt') and os.path.isfile(file_path):
        # 파일 내용을 읽어서 내용이 비어있으면 리스트에 추가합니다.
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                empty_files.append(filename)

# 빈 텍스트 파일 이름 목록을 출력합니다.
print("빈 텍스트 파일 목록:")
for empty_file in empty_files:
    print(empty_file)

print(len(empty_files))

# 예시 리스트
file_list = empty_files

# 모든 항목을 순회하면서 확장자 변경
new_file_list = [filename.replace('.txt', '.jpg') for filename in file_list]

# 변경된 리스트 출력
print(new_file_list)

folder_path = rf'C:\Users\hong_\Desktop\tubeSkin_labeling.v1i.yolov5pytorch\valid\images'  # 폴더 경로를 여기에 입력하세요.
file_names_to_delete = new_file_list  # 삭제할 파일 이름 목록을 여기에 입력하세요.

for filename in file_names_to_delete:
    file_path = os.path.join(folder_path, filename)
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"{filename} 파일을 삭제했습니다.")
        except Exception as e:
            print(f"{filename} 파일을 삭제하는 중 오류가 발생했습니다: {str(e)}")
    else:
        print(f"{filename} 파일을 찾을 수 없습니다.")
