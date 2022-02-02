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


def btn_f():
    global num_t  # num_t 변수를 전역변수로 지정
    num_t = int(ent.get())  # 입력창에 입력된 문자열을 숫자로 바꿔서 저장
    # 3개의 위젯이 요소로 있는 리스트 [label, entry, button]
    for widget in win.grid_slaves():
        widget.destroy()  # 위젯 요소를 차례로 파괴합니다.
    win.geometry("500x500")  # 창의 크기를 500x500로 설정합니다.


btn = Button(win)
btn.config(text="시작")
btn.config(command=btn_f)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()
