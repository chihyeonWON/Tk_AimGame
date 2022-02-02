from tkinter import *
win = Tk()
win.title("AIM_GAME")
win.geometry("550x150")
win.option_add("*Font", "궁서 20")

# Label
lab = Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=20)

# Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

# Button
btn = Button(win)
btn.config(text="시작")
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()
