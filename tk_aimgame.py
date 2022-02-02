from tkinter import *
import random
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

count = 1

# 버튼을 클릭했을 때 이전 버튼을 삭제하고 새로운 버튼을 생성하는 함수


def other_btn():
    global count
    # 카운트된 버튼의 숫자가 입력창에 입력한 숫자보다 작을 때
    if count < num_t:
        count += 1
        btn.destroy()
        ran_btn()
    else:  # 새로 버튼을 실행하지 않도록 설정
        btn.destroy()
        lab = Label(win)
        lab.config(text="clear")
        lab.pack(pady=230)
# 랜덤한 위치에 버튼을 생성하는 함수


def ran_btn():
    global btn
    btn = Button(win)
    btn.config(bg="red")
    btn.config(command=other_btn)
    btn.config(text=count)
    btn.place(relx=random.random(), rely=random.random())

# 버튼을 클릭했을 때 위젯을 모두 없애고 창크기를 키워주는 함수


def btn_f():
    global num_t  # num_t 변수를 전역변수로 지정
    num_t = int(ent.get())  # 입력창에 입력된 문자열을 숫자로 바꿔서 저장
    # 3개의 위젯이 요소로 있는 리스트 [label, entry, button]
    for widget in win.grid_slaves():
        widget.destroy()  # 위젯 요소를 차례로 파괴합니다.
    win.geometry("500x500")  # 창의 크기를 500x500로 설정합니다.
    ran_btn()


btn = Button(win)
btn.config(text="시작")
btn.config(command=btn_f)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()
