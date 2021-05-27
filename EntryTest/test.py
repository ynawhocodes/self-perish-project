from tkinter import *


url_window = Tk()
url_window.title("test")

url = ["url"] * 5



def saveUrl():
    for i in entries:   
        url.append(i.get())
        print(url)

entries = [] * 5

for i in range(1,5):
    urlLabel =  Label(url_window ,text="url " + str(i)+ ": ")
    urlLabel.grid(row=i, column=0)
    en = Entry(url_window, width=64)
    en.grid(row=i, column=1)
    entries.append(en)

save_btn = Button(url_window, text="저장", command=lambda: saveUrl())
save_btn.grid(row=19, column=2)

    
url_window.mainloop()