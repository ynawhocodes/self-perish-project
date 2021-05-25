from tkinter import *
from tkinter import filedialog
import os
from datetime import datetime
import cv2, numpy as np

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

    # 초기화
    global top
    top = ["top"] * imageNum
    global marginLeft
    marginLeft = ["ml"] * imageNum
    global width
    width = ["width"] * imageNum
    global height
    height = ["height"] * imageNum

    # 초기화
    global url
    url = ["url"] * imageNum

def openFolder():
    window.dirName=filedialog.askdirectory()
    global filePath
    filePath = str(window.dirName)
    changeFileName()

    img = cv2.imread(filePath + "\\img_1.jpg")
    global imageHeight, imageWidth, imageChannel
    imageHeight, imageWidth, imageChannel = img.shape

def inputUrl():
    url_window = Toplevel(window)
    url_window.title("input URL")
    url_window.resizable(False, False)
      
    for i in linkImageNum:
        urlLabel = Label(url_window , text="url " + str(i)+ ": ")
        urlLabel.grid(row=i, column=0)
        urlEntry = Entry(url_window, width=64)
        urlEntry.grid(row=i, column=1)

        URL = urlEntry.get()
        url[int(i)] = URL

    if(chk_state.get() == True):
        video_num = Label(url_window , text="비디오 삽입된 이미지 번호")
        video_url = Label(url_window , text="비디오 url")

        video_num_entry = Entry(url_window, width=64)
        video_url_entry = Entry(url_window, width=64)

        video_num.grid(row=10, column=0)
        video_url.grid(row=11, column=0)

        video_num_entry.grid(row=10, column=1)
        video_url_entry.grid(row=11, column=1)

        videoImageNum = video_num_entry.get()
        videoUrl =  video_url_entry.get()
        #비디오가 있는 이미지에는 이동url이 없을 것이므로 같은 리스트를 이용
        url[int(videoImageNum)] = videoUrl
   
    save_btn = Button(url_window, text="저장")
    save_btn.grid(row=20, column=0, columnspan=2)




# 이미지 개수
parameter = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute)


def setPosition():
    global linkImageNum
    linkImageNum = list(link_img_num_entry.get().split())
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

def saveFile():
    savePC()
    saveMB()

def savePC():
    outfile = open(filePath + "\\sp.html", "w")
    # 전체 틀 코드도 작성해야함
    outfile.write("<style>\n    .n-detail-special {background-color:#" + bgColor + ";}")
    style(top, marginLeft, width, height, "px")
    blockCode()

    outfile.close()

def saveMB():
    outfile = open(filePath  + "\\sp-m.html", "w")
        
    pcToM(marginLeft, top)
    pcToM(width, height)

    # mobile
    # 전체 틀 코드도 작성해야함
    outfile.write("<style>\n")
    style(top, marginLeft, width, height, "%")
    blockCode()

    outfile.close()
        

window = Tk()
window.title("special issue")
window.geometry("320x118+1200+500")
window.resizable(False, False)


# label
folder_path = Label(window , text="이미지 경로")
link_img_num = Label(window , text="링크있는 이미지 번호")
bg_color = Label(window, text="배경색")
cyberduck_path = Label(window, text="CyberDuck 폴더명")

# label grid
folder_path.grid(row=0, column=0)
link_img_num.grid(row=1, column=0)
bg_color.grid(row=2, column=0)
cyberduck_path.grid(row=3, column=0)

# btn
folder_path_btn = Button(window, text="찾아보기", command=openFolder, width=20)
link_img_num_entry = Entry(window)
bg_color_entry = Entry(window)
cyberduck_path_entry = Entry(window)

# btn grid
folder_path_btn.grid(row=0, column=1, columnspan=6)
link_img_num_entry.grid(row=1, column=1, columnspan=6)
bg_color_entry.grid(row=2, column=1, columnspan=6)
cyberduck_path_entry.grid(row=3, column=1, columnspan=6)

# url setting
chk_state=BooleanVar()
chk_state.set(False)
video_check = Checkbutton(window, text="video", var=chk_state)
url_position_btn = Button(window, text="url위치", command=setPosition)
url_btn = Button(window, text="url입력", command=inputUrl)
preview_btn = Button(window, text="미리보기")
save_btn = Button(window, text="저장", command=saveFile)

# url grid
video_check.grid(row=5, column=0)
url_position_btn.grid(row=5, column=1)
url_btn.grid(row=5, column=2)
preview_btn.grid(row=5, column=3)
save_btn.grid(row=5, column=4)



# style 출력
def style(topList, marginLeftList, widthList, heightList, unit): 
    for i in linkImageNum:
        outfile.write("    .n-detail-special .block" + str(i) + " .link {top:" + topList[int(i)] + unit + "; margin-left:" + marginLeftList[int(i)] + unit + "; width: " + widthList[int(i)] + unit  + "; height: " + heightList[int(i)] + unit + ";}")        
        
    if(isVideo == 'y'):
        outfile.write("    .video-wrap {position:absolute; left:0; top:0%; width:92%; margin-left:4%;}\n    .n-detail-special .video-wrap .video-content {position:relative; padding-top:56.25%;}\n    .n-detail-special .video-wrap .video-content iframe {position:absolute; left:0; top:0; width:100%; height:100%;}")

    outfile.write("</style>\n")

global bgColor
bgColor = bg_color_entry.get()
global folderName
folderName = cyberduck_path_entry.get()


# pc to mb
def pcToM(pcWidthStyle, pcHeightStyle):
    for i in linkImageNum:           
        pcWidthStyle[int(i)] = format(int(pcWidthStyle[int(i)]) / 10.8, ".2f")
        pcHeightStyle[int(i)] = format(int(pcHeightStyle[int(i)]) * 100 / imageHeight, ".2f")


# 결과 코드
def blockCode():        
    for i in range(1, imageNum):
        if(chk_state.get() == True):
            if str(i) in linkImageNum:                   
                outfile.write("<div class=\"block block" + str(i) + "\"><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")             
            else:
                if(str(i) != videoImageNum):
                    outfile.write("<div class=\"block block" + str(i) + "\"><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")
                else:
                    outfile.write("<div class=\"block block" + videoImageNum + "\"><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i)+".jpg?" + parameter + "\" alt=\"\">\n        <div class=\"video-wrap\"><div class=\"video-content\">\n            <iframe src=\"https://www.youtube.com/embed/" + videoUrl + " frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n        </div>\n    </div>\n</div>")                         

        else:
            if str(i) in linkImageNum:
                outfile.write("<div class=\"block block" + str(i) + "\"><a href=\"" + url[i] + "\" class=\"link\">링크</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>")
            else:
                outfile.write("<div class=\"block block" + str(i) + "\"><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + folderName + "/img_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>")                     


window.mainloop()





