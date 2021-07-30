import os

file_path = input("이미지를 저장한 폴더 경로를 입력해주세요:")
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name) # 현재 이미지 경로
    new_name = "img_" + str(i) + ".jpg" # 새로운 이름
    new_name = os.path.join(file_path, new_name) # 경로 + 새로운 이름
    os.rename(src, new_name)
    i += 1

