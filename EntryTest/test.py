from tkinter import *


url_window = Tk()
url_window.title("test")

url = ["url"] * 10
linkImageNum = ["2", "4" , "5"]

def saveUrl():
    cnt = 0
    for i in linkImageNum:  
        print(entries[cnt].get()) 
        url[int(i)] = entries[cnt].get()
        print(url)
        cnt += 1

entries = []

for i in linkImageNum:
    urlLabel =  Label(url_window ,text="url " + str(i)+ ": ")
    urlLabel.grid(row=i, column=0)
    en = Entry(url_window, width=64)
    en.grid(row=i, column=1)
    entries.append(en)

save_btn = Button(url_window, text="저장", command=lambda: saveUrl())
save_btn.grid(row=19, column=2)

    
url_window.mainloop()