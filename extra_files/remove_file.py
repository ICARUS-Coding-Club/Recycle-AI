import os

# 검색할 폴더 경로 설정
folder_path = rf'C:\Users\hong_\Desktop\YOLOv5\recycle_dataset\valid\labels'

# 파일 이름을 저장할 빈 리스트 생성
invalid_start_filenames = []

# 지정한 폴더에서 모든 .txt 파일 가져오기
file_list = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]

# 각 텍스트 파일을 열고 내용 분석
for filename in file_list:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r') as file:
        file_contents = file.read()
        # 공백으로 분리된 데이터 가져오기
        data = file_contents.split()
        # 첫 번째 데이터가 0 또는 1이 아니면 파일 이름을 리스트에 추가
        if len(data) > 0 and data[0][0] not in ('0', '1'):
            invalid_start_filenames.append(filename)

# 조건을 만족하는 파일 삭제
for filename in invalid_start_filenames:
    file_path = os.path.join(folder_path, filename)
    os.remove(file_path)
    print(f"{filename} 파일을 삭제했습니다.")
