from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from datetime import datetime
import cv2, numpy as np

def changeFileName():
    global imageNum
    imageNum = 1
    file_names = os.listdir(filePath)
    for name in file_names:
        src = os.path.join(filePath, name) # 현재 이미지 경로
        new_name = "image_" + str(imageNum) + ".jpg" # 새로운 이름
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

videoInfo = []

def saveVideoUrl(i, URL):
    url[int(i)] = URL
    videoInfo.insert(0, i)
    videoInfo.insert(1, URL)

urlEntryList = []
videoEntryList = []

def saveUrl():
    i = 0
    for j in linkImageNum:    
        url[int(j)] = urlEntryList[i].get()
        i += 1

    url_window.destroy()
       

def inputUrl():
    global url_window
    url_window = Toplevel(window)
    url_window.title("input URL")
    url_window.resizable(False, False)
    
    global isVideo
    isVideo = chk_state.get()
    if(isVideo == True):
        video_num = Label(url_window , text="비디오 삽입된 이미지 번호")
        video_url = Label(url_window , text="비디오 url")

        global video_num_entry
        video_num_entry = Entry(url_window, width=64)
        video_url_entry = Entry(url_window, width=64)

        video_num.grid(row=0, column=0)
        video_url.grid(row=1, column=0)

        video_num_entry.grid(row=0, column=1)
        video_url_entry.grid(row=1, column=1)

        # 비디오가 있는 이미지에는 이동url이 없을 것이므로 같은 리스트를 이용
        save_btn = Button(url_window, text="저장", command=lambda: saveVideoUrl(video_num_entry.get(), video_url_entry.get()))
        save_btn.grid(row=2, column=2)

    for i in linkImageNum:     
        urlLabel = Label(url_window , text="url" + str(i)+ ": ")
        urlLabel.grid(row=i, column=0)
        urlEntry = Entry(url_window, width=64)
        urlEntry.grid(row=i, column=1)
        urlEntryList.append(urlEntry)   

    save_btn = Button(url_window, text="저장", command=lambda: saveUrl())
    save_btn.grid(row=100, column=2)
   


# 파라미터
parameter = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute)

def setPosition():
    global linkImageNum
    linkImageNum = list(link_img_num_entry.get().split())
    for i in linkImageNum:
        img = cv2.imread(filePath + "\\image_" + i + ".jpg")
        x,y,w,h	= cv2.selectROI('image', img, False)
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
    outfile = open(filePath[:-7] + "\\sp.html", "w")
    # 전체 틀
    outfile.write("<!DOCTYPE html>\n<html lang=\"ko\">\n<head>\n    <link type=\"text/css\" rel=\"stylesheet\" href=\"https://image.msscdn.net/ui/utility/event/css/common.css?202005181853\">\n    <style>* {margin:0;padding:0;} .link{background-color:rgba(212,5,5,.5)}</style>\n    <title>special issue</title>\n</head>\n<body>\n")
    outfile.write("<div class=\"n-detail-special\">\n")

    outfile.write("<style>\n    .n-detail-special {background-color:#" + bg_color_entry.get() + ";}\n")
    style(top, marginLeft, width, height, "px", outfile)
    blockCode(outfile)

    outfile.write("\n</div>\n</body>\n</html>")
    outfile.close()

def saveMB():
    outfile = open(filePath[:-7]  + "\\sp-m.html", "w")
        
    pcToM(marginLeft, top)
    pcToM(width, height)

    # 전체 틀
    outfile.write("<!DOCTYPE html>\n<html lang=\"ko\">\n<head>\n    <link type=\"text/css\" rel=\"stylesheet\" href=\"https://image.msscdn.net/ui/utility/event/css/m_common.css?202005141625\">\n    <style>* {margin:0;padding:0;} img{max-width:100%; vertical-align: top; border:0;} .link{background-color:rgba(212,5,5,.5)}</style>\n    <title>special issue</title>\n</head>\n<body>\n")
    outfile.write("<div class=\"n-detail-special\">\n")
    
    outfile.write("<style>\n")
    style(top, marginLeft, width, height, "%", outfile)
    blockCode(outfile)

    outfile.write("\n</div>\n</body>\n</html>")
    outfile.close()

def preview():
    os.startfile(filePath[:-7])

def previewPC():
    os.startfile(filePath[:-7] + "\\sp.html")

def previewMB():
    os.startfile(filePath[:-7] + "\\sp-m.html")

window = Tk()
window.title("special issue")
window.geometry("279x144+1200+500")
window.resizable(False, False)


# label
folder_path = Label(window , text="이미지 경로")
link_img_num = Label(window , text="링크있는 이미지 번호")
bg_color = Label(window, text="배경색 (# 빼고)")
cyberduck_path = Label(window, text="CyberDuck 폴더명")
preview_state=BooleanVar()
preview_state.set(False)
preview_check = Label(window , text="미리보기")

# label grid
folder_path.grid(row=0, column=0)
link_img_num.grid(row=3, column=0)
bg_color.grid(row=2, column=0)
cyberduck_path.grid(row=1, column=0)
preview_check.grid(row=6, column=0)


# btn
folder_path_btn = Button(window, text="찾아보기", command=openFolder, width=20)
link_img_num_entry = Entry(window)
bg_color_entry = Entry(window)
cyberduck_path_entry = Entry(window)

preview_btn = Button(window, text="폴더열기", command=preview, width=6)
previewPC_btn = Button(window, text="PC", command=previewPC, width=6)
previewMB_btn = Button(window, text="MB", command=previewMB, width=6)
   

# btn grid
folder_path_btn.grid(row=0, column=1, columnspan=6)
link_img_num_entry.grid(row=3, column=1, columnspan=6)
bg_color_entry.grid(row=2, column=1, columnspan=6)
cyberduck_path_entry.grid(row=1, column=1, columnspan=6)
preview_btn.grid(row=6, column=1)
previewPC_btn.grid(row=6, column=2)
previewMB_btn.grid(row=6, column=3)

# url setting
chk_state=BooleanVar()
chk_state.set(False)
video_check = Checkbutton(window, text="video", var=chk_state)
url_position_btn = Button(window, text="url위치", command=setPosition, width=6)
url_btn = Button(window, text="url입력", command=inputUrl, width=6)
save_btn = Button(window, text="저장", command=saveFile, width=6)



# url grid
video_check.grid(row=5, column=0)
url_position_btn.grid(row=5, column=1)
url_btn.grid(row=5, column=2)
save_btn.grid(row=5, column=3)


# style 출력
def style(topList, marginLeftList, widthList, heightList, unit, outfile): 
    for i in linkImageNum:
        outfile.write("    .n-detail-special .block" + str(i) + " .link {top:" + topList[int(i)] + unit + "; margin-left:" + marginLeftList[int(i)] + unit + "; width: " + widthList[int(i)] + unit  + "; height: " + heightList[int(i)] + unit + ";}\n")        
        
    if(isVideo == True):
        if(unit == "%"):
            outfile.write("    .video-wrap {position:absolute; left:0; top:0%; width:100%; height:100% margin-left:0%;}\n    .n-detail-special .video-wrap .video-content {position:relative; padding-top:56.25%;}\n    .n-detail-special .video-wrap .video-content iframe {position:absolute; left:0; top:0; width:100%; height:100%;}\n")
        else:
            outfile.write("    .n-detail-special .video-wrap {position:absolute;left:50%;top:0%;width:1080px;height:608px; margin-left:-540px;}\n    .n-detail-special .video-wrap iframe {position:absolute;left:0;top:0;width:100%;height:100%;}\n")
    outfile.write("</style>\n")


# pc to mb
def pcToM(pcWidthStyle, pcHeightStyle):
    for i in linkImageNum:
        img = cv2.imread(filePath + "\\image_" + i + ".jpg")

        imageHeight, imageWidth, imageChannel = img.shape
       
        pcWidthStyle[int(i)] = format(int(pcWidthStyle[int(i)]) / 10.8, ".2f")
        pcHeightStyle[int(i)] = format(int(pcHeightStyle[int(i)]) * 100 / imageHeight, ".2f")

# 결과 코드
def blockCode(outfile):        
    for i in range(1, imageNum - 1):
        if(isVideo == True):
            if str(i) in linkImageNum:            
                outfile.write("<div class=\"block block" + str(i) + "\"><a href=\"" + url[i] + "\" class=\"link\">link</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + cyberduck_path_entry.get() + "/image_" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>\n")             
            else:
                if(str(i) !=  videoInfo[0]):   
                    outfile.write("<div class=\"block block" + str(i) + "\"><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + cyberduck_path_entry.get() + "/image_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>\n")
                else:  
                    outfile.write("<div class=\"block block" +  videoInfo[0] + "\">\n<img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + cyberduck_path_entry.get() + "/image_" + str(i)+".jpg?" + parameter + "\" alt=\"\">\n    <div class=\"video-wrap\">\n        <div class=\"video-content\">\n            <iframe src=\"https://www.youtube.com/embed/" + videoInfo[1] + "\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n        </div>\n    </div>\n</div>\n")                         

        else:
            if str(i) in linkImageNum:   
                outfile.write("<div class=\"block block" + str(i) + "\"><a href=\"" + url[i] + "\" class=\"link\">link</a><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + cyberduck_path_entry.get() + "/image_" + str(i)+".jpg?" + parameter + "\" alt=\"\"></div>\n")
            else:   
                outfile.write("<div class=\"block block" + str(i) + "\"><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + cyberduck_path_entry.get() + "/image_" + str(i) + ".jpg?" + parameter + "\" alt=\"\"></div>\n")                     
   
   
    outfile.write("\n\n\n<!-- event -->\n<div class=\"block block" + str(imageNum - 1) + "\"><img src=\"https://image.msscdn.net/musinsaUI/specialissue/" + cyberduck_path_entry.get() + "/image_" + str(imageNum - 1) + ".jpg?" + parameter + "\" alt=\"\"></div>\n<!-- //event -->\n\n")

window.mainloop()


















