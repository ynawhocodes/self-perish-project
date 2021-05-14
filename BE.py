imageName = input("이미지명을 입력해주세요: ")
imageNum = int(input("이미지 개수를 입력하세요: "))
parameter = input("파라미터 값을 입력해주세요: ")
a = int(input("링크있는 이미지 번호를 적어주세요 (ex. 3, 5, 11)"))
folderName = input("폴더명을 입력해주세요: ")


def alink(imageNum):
    return("<a href=\"" + url + "\" class=\"link\">링크</a>"





for i in range(imageNum):
    if i < 10:
        print("<div class=\"block block0" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/" + imageName +  str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
    else:
        print("<div class=\"block block" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/" + imageName +  str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
