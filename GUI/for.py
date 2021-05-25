from tkinter import *
from tkinter import filedialog



window = Tk()
window.title("special issue")
window.geometry("500x500+1050+500")
window.resizable(False, True)


#오로지 test. main과 logic 같지 않음
urlLabel = [""] * 5 
urlEntry = [""] * 5 

for i in range(0, 5):
    urlLabel = Label(window , text="url " + str(i)+ ": ")
    urlLabel.grid(row=i, column=0)
    urlEntry = Entry(window, width=64)
    urlEntry.grid(row=i, column=1)




b2 = Button(window, text="저장")

b2.grid(row=7, column=1, columnspan=2)





window.mainloop()



