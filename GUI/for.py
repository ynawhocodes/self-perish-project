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
    url_window = Tk().Toplevel(window)

    url_window = Tk()
    url_window.title("special issue")
    url_window.geometry("70x118+1200+500")
    url_window.resizable(False, False)

    url_window.mainloop()
              


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

folder_path_btn = Button(window, text="찾아보기", command=openFolder, width=17)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

folder_path_btn.grid(row=0, column=1, columnspan=5)
e1.grid(row=1, column=1, columnspan=5)
e2.grid(row=2, column=1, columnspan=5)
e3.grid(row=3, column=1, columnspan=5)

chk_state=BooleanVar()
chk_state.set
video_check = Checkbutton(window, text="video", var=chk_state,)
url_btn = Button(window, text="url입력", command=inputUrl)
b1 = Button(window, text="미리보기", command=process)
b2 = Button(window, text="저장")

video_check.grid(row=5, column=0)
b1.grid(row=5, column=1)
url_btn.grid(row=5, column=2)
b1.grid(row=5, column=3)
b2.grid(row=5, column=4)





window.mainloop()



