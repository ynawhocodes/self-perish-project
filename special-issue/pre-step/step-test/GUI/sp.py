from tkinter import *
from tkinter import filedialog

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0, str(mytemp))

def openFolder():
    window.dirName=filedialog.askdirectory()
    print(window.dirName)

def inputUrl():
    url_window = Toplevel(window)
    url_window.title("input URL")
    url_window.resizable(False, False)
      
    #오로지 test. main과 logic 같지 않음
    urlLabel = [""] * 5 
    urlEntry = [""] * 5 

    for i in range(0, 5):
        urlLabel = Label(url_window , text="url " + str(i)+ ": ")
        urlLabel.grid(row=i, column=0)
        urlEntry = Entry(url_window, width=64)
        urlEntry.grid(row=i, column=1)


    video_num = Label(url_window , text="비디오 삽입된 이미지 번호")
    video_url = Label(url_window , text="비디오 url")

    e1 = Entry(url_window, width=64)
    e2 = Entry(url_window, width=64)

    video_num.grid(row=6, column=0)
    video_url.grid(row=7, column=0)

    e1.grid(row=6, column=1)
    e2.grid(row=7, column=1)

    b2 = Button(url_window, text="저장")
    b2.grid(row=8, column=0, columnspan=2)



window = Tk()
window.title("special issue")
window.geometry("320x118+1200+500")
window.resizable(False, False)

folder_path = Label(window , text="이미지 경로")
link_img_num = Label(window , text="링크있는 이미지 번호")
bg_color = Label(window, text="배경색")
cyberduck_path = Label(window, text="CyberDuck 폴더명")

folder_path.grid(row=0, column=0)
link_img_num.grid(row=1, column=0)
bg_color.grid(row=2, column=0)
cyberduck_path.grid(row=3, column=0)

folder_path_btn = Button(window, text="찾아보기", command=openFolder, width=20)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

folder_path_btn.grid(row=0, column=1, columnspan=6)
e1.grid(row=1, column=1, columnspan=6)
e2.grid(row=2, column=1, columnspan=6)
e3.grid(row=3, column=1, columnspan=6)

chk_state=BooleanVar()
chk_state.set
video_check = Checkbutton(window, text="video", var=chk_state,)
url_position_btn = Button(window, text="url위치", command=inputUrl)
url_btn = Button(window, text="url입력", command=inputUrl)
b1 = Button(window, text="미리보기", command=process)
b2 = Button(window, text="저장")

video_check.grid(row=5, column=0)
url_position_btn.grid(row=5, column=1)
url_btn.grid(row=5, column=2)
b1.grid(row=5, column=3)
b2.grid(row=5, column=4)





window.mainloop()



