from tkinter import *

window = Tk()

window.title("기획전")
window.geometry("1400x800+500+200")
window.resizable(False, False)

settingFrame = LabelFrame(window, text="setting")
settingFrame.pack(fill=BOTH, ipadx=300, side=LEFT)              

resultFrame = LabelFrame(window, text="result", relief="solid", bd=2, background="white")
resultFrame.pack(fill=BOTH, ipadx=400, side=RIGHT)       







window.mainloop()

