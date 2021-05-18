print("\n----------------------------[설정]------------------------------------------\n")

# imageName = input("\n이미지명을 입력해주세요: ")
imageNum = int(input("\n이미지 개수를 입력하세요: "))
imageHeight = int(input("\n이미지 공통 분할 높이를 입력하세요: "))
parameter = input("\n파라미터 값을 입력해주세요: ")
linkImageNum = list(input("\n링크있는 이미지 번호를 입력해주세요 (ex. 3 5 11): ").split())
folderName = input("\n폴더명을 입력해주세요: ")

# 비디오 설정
print("\n\n[비디오 설정]")
isVideo = input("\n유튜브영상이 삽입되나요? (y/n): ")

# 초기화
url = ["url"] * imageNum

if(isVideo == 'y'):
    videoImageNum = input("\n영상이 삽입되는 이미지 번호를 입력해주세요: ")
    videoUrl = input("\n유튜브 링크 뒷부분 입력해주세요(https://www.youtube.com/embed/[이부분]: ")

    #비디오가 있는 이미지에는 이동url이 없을 것이므로 같은 리스트를 이용
    url[int(videoImageNum)] = videoUrl

print("\n----------------------------[URL입력]------------------------------------------\n")

def inputUrl():
    for i in linkImageNum:
        URL = input("\nimg " + i + " 번의 url를 입력해주세요: ")
        url[int(i)] = URL

# style 출력
def style(topList, marginLeftList, unit): 
    for i in linkImageNum:
        print("    .n-detail-special .block" + i + " .link {top:" + topList[int(i)] + unit + "; margin-left:" + marginLeftList[int(i)] + unit + ";}")        
    print("    .n-detail-special .block" +  str(imageNum - 1) + ".link{top:40%; width:100%; height:20%; margin-left:-50%;}")

    if(isVideo == 'y'):
        print("    .video-wrap {position:absolute; left:0; top:0%; width:92%; margin-left:4%;}\n    .n-detail-special .video-wrap .video-content {position:relative; padding-top:56.25%;}\n    .n-detail-special .video-wrap .video-content iframe {position:absolute; left:0; top:0; width:100%; height:100%;}")

    print("</style>\n")

inputUrl()
# 비디오 설정
print("\n\n[배경색 설정]")
bgColor = input("\npc 배경색을 입력해주세요(#빼고): ")


print("\n----------------------------[위치 잡기]------------------------------------------\n")

# mobile to pc
def mToPc(topList, marginLeftList):
    for i in linkImageNum:    
        topList[int(i)] = format(int(topList[int(i)]) * imageHeight / 100, ".2f")
        marginLeftList[int(i)] = format(int(marginLeftList[int(i)]) * 10.8, ".2f")

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
            if(isVideo == 'y'): # 보통 유튜브는 10 이하에 위치해 있으므로(예외 가능성 있음)
                if str(i) in linkImageNum:                   
                    print("<div class=\"block block0" + str(i) + "><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_0" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")             
                else:
                    if(str(i) != videoImageNum):
                        print("<div class=\"block block0" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_0" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
                    else:
                        print("<div class=\"block block0" + videoImageNum + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_0" + str(i)+".jpg?" + parameter + "\" alt=\"\">\n        <div class=\"video-wrap\"><div class=\"video-content\">\n            <iframe src=\"https://www.youtube.com/embed/" + videoUrl + " frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n        </div>\n    </div>\n</div>")          

                    

            else:
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