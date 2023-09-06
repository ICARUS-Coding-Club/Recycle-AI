import os

def detectTrash(id):
    # 쓰레기 클래스
    trash_dict = {
        0: "glass",
        1: "pet",
        2: "styrofoam",
        3: "can",
        4: "milkCarton",
        5: "paperCup",
        6: "paper",
        7: "box",
        8: "plasticBag",
        9: "battery",
        10: "rubberGloves",
        11: "lamp",
        12: "cosmeticTube",
        13: "detergentTube",
        14: "fruitPackingNet"
    }

    # user id 받기
    user_id = id

    # 텍스트 파일 초기화
    file_path = rf"yolov5-master\runs\detect\trash\labels\{user_id}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("")

    # 이미지 판별
    command = rf"python ./yolov5-master/detect.py --weights ./yolov5-master/runs/train/yolov5_trash_final/weights/best.pt --img 640 --conf 0.5 --source ./images/{user_id}.jpg --save-txt --name trash --exist-ok"
    os.system(command)

    result = []
    # 파일을 읽기 모드로 엽니다.
    with open(file_path, "r", encoding="utf-8") as file:
        # 파일의 각 줄을 순회하면서 데이터를 처리합니다.
        for line in file:
            # 각 줄을 공백을 기준으로 분리합니다.
            parts = line.split()
            
            # 첫 번째 숫자를 추출합니다.
            first_number = int(parts[0])
            
            result.append(trash_dict[first_number])

    return result

detectTrash('user_id')