
print("\n----------------------------[설정]------------------------------------------\n")

imageName = input("\n이미지명을 입력해주세요: ")
imageNum = int(input("\n이미지 개수를 입력하세요: "))
parameter = input("\n파라미터 값을 입력해주세요: ")
linkImageNum = list(input("\n링크있는 이미지 번호를 적어주세요 (ex. 3 5 11): ").split())
folderName = input("\n폴더명을 입력해주세요: ")
   
print("\n----------------------------[URL입력]------------------------------------------\n")


url = ["url"] * imageNum

def inputUrl():
    for i in linkImageNum:
        URL = input("\nimg " + i + " 번의 url를 입력해주세요: ")
        url[int(i)] = URL

inputUrl()

print("\n\n--------------------------------[결과]--------------------------------------\n\n")

for i in range(1, imageNum):
    if i < 10:
        if str(i) in linkImageNum:
            print("<div class=\"block block0" + str(i) + "><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/" + imageName + "_0" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")
        else:
            print("<div class=\"block block0" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/" + imageName +  "_0" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
                    
    else:
        if str(i) in linkImageNum:
            print("<div class=\"block block" + str(i) + "><a href=\"" +  url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/" + imageName + "_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
        else:
            print("<div class=\"block block" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/" + imageName +  "_" +  str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
 
