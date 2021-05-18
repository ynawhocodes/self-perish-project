
print("\n----------------------------[설정]------------------------------------------\n")

# imageName = input("\n이미지명을 입력해주세요: ")
imageNum = int(input("\n이미지 개수를 입력하세요: "))
parameter = input("\n파라미터 값을 입력해주세요: ")
linkImageNum = list(input("\n링크있는 이미지 번호를 입력해주세요 (ex. 3 5 11): ").split())
folderName = input("\n폴더명을 입력해주세요: ")
   
print("\n----------------------------[URL입력]------------------------------------------\n")

# 초기화
url = ["url"] * imageNum

def inputUrl():
    for i in linkImageNum:
        URL = input("\nimg " + i + " 번의 url를 입력해주세요: ")
        url[int(i)] = URL

# style 출력
def style(topList, marginLeftList, unit): 
    for i in linkImageNum:
        print("    .n-detail-special .block" + i + " .link {top:" + topList[int(i)] + unit + "; margin-left:" + marginLeftList[int(i)] + unit + ";}")
    
    print("    .n-detail-special .block" +  str(imageNum - 1) + ".link{top:40%; width:100%; height:20%; margin-left:-50%;}")
    print("</style>\n")

inputUrl()
bgColor = input("\npc 배경색을 입력해주세요(#빼고): ")


print("\n----------------------------[위치 잡기]------------------------------------------\n")

# mobile to pc
def mToPc(topList, marginLeftList):
    for i in linkImageNum:    
        topList[int(i)] = str(int(topList[int(i)]) * 20)
        marginLeftList[int(i)] = str(int(marginLeftList[int(i)]) * 20)

# 초기화
top = ["top"] * imageNum
marginLeft = ["ml"] * imageNum

def inpuPosition():
    print("mobile버전의 링크 위치를 입력해주세요")
    for i in linkImageNum:
        print("\n>img " + i + " 번--- ")
        TOP = input("top: ")
        top[int(i)] = TOP

        ML = input("margin-left: ")
        marginLeft[int(i)] = ML

inpuPosition()

print("\n\n--------------------------------[결과]--------------------------------------\n\n")

def blockCode():        
    for i in range(1, imageNum + 1):
        if i < 10:
            if str(i) in linkImageNum:
                print("<div class=\"block block0" + str(i) + "><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_0" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")
            else:
                print("<div class=\"block block0" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_0" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
                        
        else:
            if str(i) in linkImageNum:
                print("<div class=\"block block" + str(i) + "><a href=\"" +  url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
            else:
                print("<div class=\"block block" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" +  str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
    

# pc
print("\n***************PC code*******************\n")
print("<style>\n    .n-detail-special {background-color:#" + bgColor + ";}")
style(top, marginLeft, "%")
blockCode()

# mobile
print("\n***************MOBILE mobile*******************\n")

# top, margin-left 모바일 비율로 변경
mToPc(top, marginLeft)
   
print("<style>\n    .n-detail-special .link {width:25%; min-height:50px;}")
style(top, marginLeft, "px")
blockCode()