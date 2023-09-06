import os

images_folder = rf'C:\Users\hong_\Desktop\YOLOv5\recycle_dataset\valid\images'
labels_folder = rf'C:\Users\hong_\Desktop\YOLOv5\recycle_dataset\valid\labels'

# images 폴더와 labels 폴더 내의 파일 이름을 가져옵니다.
images_files = set(os.listdir(images_folder))
labels_files = set(os.listdir(labels_folder))

# 확장자를 제외한 파일 이름을 추출합니다.
images_filenames_no_ext = {os.path.splitext(filename)[0] for filename in images_files}
labels_filenames_no_ext = {os.path.splitext(filename)[0] for filename in labels_files}

# 확장자를 제외한 파일 이름을 비교하여 삭제할 파일을 찾습니다.
files_to_delete = images_filenames_no_ext.symmetric_difference(labels_filenames_no_ext)

# 삭제할 파일을 하나씩 처리합니다.
for file_to_delete in files_to_delete:
    if file_to_delete in images_filenames_no_ext:
        os.remove(os.path.join(images_folder, file_to_delete + '.jpg'))
        print(f"Deleted {file_to_delete}.jpg from 'images' folder.")
    if file_to_delete in labels_filenames_no_ext:
        os.remove(os.path.join(labels_folder, file_to_delete + '.txt'))
        print(f"Deleted {file_to_delete}.txt from 'labels' folder.")
