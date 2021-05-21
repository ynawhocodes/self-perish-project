from tkinter import *
from tkinter import filedialog
import os
from datetime import datetime
import cv2, numpy as np


def openFolder():
    window.dirName=filedialog.askdirectory()

window = Tk()
window.title("special issue")
window.geometry("270x118+1200+500")
window.resizable(False, False)

folder_path = Label(window , text="이미지 경로")
link_img_num = Label(window , text="링크있는 이미지 번호")
bg_color = Label(window, text="배경색")
cyberduck_path = Label(window, text="CyberDuck 폴더명")

folder_path.grid(row=0, column=0)
link_img_num.grid(row=1, column=0)
bg_color.grid(row=2, column=0)
cyberduck_path.grid(row=3, column=0)

folder_path_btn = Button(window, text="찾아보기", command=openFolder)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

folder_path_btn.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)


b1 = Button(window, text="미리보기")
b2 = Button(window, text="저장")
b1.grid(row=5, column=0)
b2.grid(row=5, column=1)

window.mainloop()


# 이미지 개수
parameter = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute)
filePath = str(window.dirName)

def changeFileName():
    global imageNum
    imageNum = 1
    file_names = os.listdir(filePath)
    for name in file_names:
        src = os.path.join(filePath, name) # 현재 이미지 경로
        new_name = "img_" + str(imageNum) + ".jpg" # 새로운 이름
        new_name = os.path.join(filePath, new_name) # 경로 + 새로운 이름
        os.rename(src, new_name)
        imageNum += 1

changeFileName()

img = cv2.imread(filePath + "\\img_1.jpg")
imageHeight, imageWidth, imageChannel = img.shape

print("\n----------------------------[설정]------------------------------------------\n")
linkImageNum = list(input(e1.get()).split())


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

print("\n----------------------------[위치 잡기]------------------------------------------\n")\

# 초기화
top = ["top"] * imageNum
marginLeft = ["ml"] * imageNum
width = ["width"] * imageNum
height = ["height"] * imageNum

for i in linkImageNum:
    img = cv2.imread(filePath + "\\img_" + i + ".jpg")
    x,y,w,h	= cv2.selectROI('img', img, False)
    if w and h:
        roi = img[y:y+h, x:x+w]  
        top[int(i)] = str(y)
        marginLeft[int(i)] = str(int(x)- 540)
        width[int(i)] = str(w)
        height[int(i)] = str(h)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("\n----------------------------[URL입력]------------------------------------------\n")

def inputUrl():
    for i in linkImageNum:
        URL = input("\nimg " + i + " 번의 url를 입력해주세요: ")
        url[int(i)] = URL

# style 출력
def style(topList, marginLeftList, widthList, heightList, unit): 
    for i in linkImageNum:
        print("    .n-detail-special .block" + str(i) + " .link {top:" + topList[int(i)] + unit + "; margin-left:" + marginLeftList[int(i)] + unit + "; width: " + widthList[int(i)] + unit  + "; height: " + heightList[int(i)] + unit + ";}")        
        
    if(isVideo == 'y'):
        print("    .video-wrap {position:absolute; left:0; top:0%; width:92%; margin-left:4%;}\n    .n-detail-special .video-wrap .video-content {position:relative; padding-top:56.25%;}\n    .n-detail-special .video-wrap .video-content iframe {position:absolute; left:0; top:0; width:100%; height:100%;}")

    print("</style>\n")

inputUrl()
# 비디오 설정
print("\n\n[배경색 설정]")
bgColor = e2.get()
folderName = e3.get()


# pc to mb
def pcToM(pcWidthStyle, pcHeightStyle):
    for i in linkImageNum:           
        pcWidthStyle[int(i)] = format(int(pcWidthStyle[int(i)]) / 10.8, ".2f")
        pcHeightStyle[int(i)] = format(int(pcHeightStyle[int(i)]) * 100 / imageHeight, ".2f")


print("\n\n--------------------------------[결과]--------------------------------------\n\n")

def blockCode():        
    for i in range(1, imageNum):
        if(isVideo == 'y'):
            if str(i) in linkImageNum:                   
                print("<div class=\"block block" + str(i) + "><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")             
            else:
                if(str(i) != videoImageNum):
                    print("<div class=\"block block" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
                else:
                    print("<div class=\"block block" + videoImageNum + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i)+".jpg?" + parameter + "\" alt=\"\">\n        <div class=\"video-wrap\"><div class=\"video-content\">\n            <iframe src=\"https://www.youtube.com/embed/" + videoUrl + " frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n        </div>\n    </div>\n</div>")                         

        else:
            if str(i) in linkImageNum:
                print("<div class=\"block block" + str(i) + "><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")
            else:
                 print("<div class=\"block block" + str(i) + "><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")                     

# pc
print("\n***************PC code*******************\n")
print("<style>\n    .n-detail-special {background-color:#" + bgColor + ";}")
style(top, marginLeft, width, height, "px")
blockCode()

# mobile
print("\n***************MOBILE mobile*******************\n")

pcToM(marginLeft, top)
pcToM(width, height)
   
print("<style>\n")
style(top, marginLeft, width, height, "%")
blockCode()

