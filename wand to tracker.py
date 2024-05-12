import json
import os

# 사용자로부터 파일 경로를 입력받음
input_file_path = input("수정할 JSON 파일의 경로를 입력해주세요: ")

# 파일 경로와 확장자를 분리
file_path_without_extension, file_extension = os.path.splitext(input_file_path)

# 파일명 뒷부분에 '_track'를 추가하여 새로운 파일 경로 생성
output_file_path = f"{file_path_without_extension}_track{file_extension}"

# 파일을 열어 JSON 데이터를 로드
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# JSON 데이터에서 원하는 문자열을 찾아 변경
if isinstance(data, dict):  # 데이터가 딕셔너리인 경우
    keys_to_modify = list(data.keys())  # 딕셔너리 키 리스트 복사
    for key in keys_to_modify:
        if data[key] == "controller":
            data[key] = "generic_tracker"
        elif data[key] == "Vive. Controller MV":
            data[key] = "Vive Tracker PVT"
        elif data[key] == "vr_controller_vive_1_5":
            data[key] = "vr_tracker_vive_1_0"
    
    if "revision" in data and data["revision"] == 1:
        data["tracked_controller_role"] = ""

# 변경된 데이터를 새 파일에 작성
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"파일이 성공적으로 수정되어 {output_file_path}에 저장되었습니다.")
