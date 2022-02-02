# Tk_AimGame
tkinter와 Python 언어로 에임(조준) 연습하는 게임 만들기 (exe파일)

## 시작 창화면 구성 및 설계

### 구현할 기능     
   
표적의 등장 개수를 entry 입력창에 입력합니다.   
   
아래의 시작 버튼을 누르면 게임 화면으로 넘어갑니다.
 
 ### 처음에 등장하는 창 생성
 
 ```python
 from tkinter import *
win = Tk()
win.title("AIM_GAME")
win.geometry("550x150")
win.option_add("*Font", "궁서 20")


win.mainloop()
```   
![aimgame_window](https://user-images.githubusercontent.com/58906858/152107147-7acb16f2-6249-4ba2-8b44-147df3734174.png)

### 이제 여기에 표적 개수를 글자를 표시하기 위해 라벨을 하나 만들어 줍니다.   
   
위치는 grid()함수를 사용합니다.   
```python
# Label
lab = Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=20)
```   
![aimgame_rabel](https://user-images.githubusercontent.com/58906858/152107558-c676a277-aa9a-47b2-bbcd-ef785328f27b.png)   
   
### 표적 개수를 입력하는 입력창을 만들어 줍니다.
   
위치는 마찬가지로 grid()함수를 사용합니다.   
```python
# Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)
```   
![aimgame_entry](https://user-images.githubusercontent.com/58906858/152107788-7bb29a1f-e06b-413f-a63b-9e39feec1514.png)   

## 시작 버튼을 만들어 줍니다.

```python
# Button
btn = Button(win)
btn.config(text="시작")
btn.grid(column=0, row=1, columnspan=2)
```   
![aimgame_button](https://user-images.githubusercontent.com/58906858/152108711-fb79a520-35db-4509-825b-ca5b886a28ef.png)

### 버튼이 눌러졌을 때 실행할 함수 생성

버튼이 눌러졌을 때 entry에 입력된 숫자를 변수에 저장하고 모든 위젯을 화면에서 없앰과 동시에 화면 크기를 키우는 함수를 구현합니다.   
```python
def btn_f():
    global num_t # num_t 변수를 전역변수로 지정
    num_t = int(ent.get()) # 입력창에 입력된 문자열을 숫자로 바꿔서 저장
    for widget in win.grid_slaves(): # 3개의 위젯이 요소로 있는 리스트 [label, entry, button]
        widget.destroy() # 위젯 요소를 차례로 파괴합니다.
    win.geometry("500x500") 
```

만들어진 btn_f 함수를 버튼의 커맨드옵션으로 버튼이 클릭됬을 때 실행되도록 합니다.
```python
btn.config(command=btn_f)
```   
   
버튼을 클릭하면 모든 위젯이 화면에서 사라지고 화면의 크기가 커집니다.
   
### 버튼이 눌러졌을 때 랜덤한 위치에 버튼을 생성하는 함수 생성   
   
먼저 random 모듈을 사용하기위해 import 해줍니다.
```python
import random
```   
   
랜덤한 위치에 버튼을 생성하는 함수를 생성하고  btn_f 안에서 함수를 실행합니다.
```python
def ran_btn():
    btn = Button(win)
    btn.config(bg="red")
    btn.place(relx=random.random(), rely=random.random())
    
def btn_f():
    global num_t  # num_t 변수를 전역변수로 지정
    num_t = int(ent.get())  # 입력창에 입력된 문자열을 숫자로 바꿔서 저장
    # 3개의 위젯이 요소로 있는 리스트 [label, entry, button]
    for widget in win.grid_slaves():
        widget.destroy()  # 위젯 요소를 차례로 파괴합니다.
    win.geometry("500x500")  # 창의 크기를 500x500로 설정합니다.
    ran_btn()
    
```   
   
입력창에 숫자를 입력하고 시작버튼을 누르면 위젯이 사라지고 창이 커짐과 동시에 화면의 랜덤한 위치에 버튼이 생성됩니다.   
   
![aimgame_random](https://user-images.githubusercontent.com/58906858/152111134-06e3afb2-767d-4c88-a1e8-eed46e616cec.png)

### 랜덤한 위치에 생성된 버튼을 제거하고 새로운 버튼을 만드는 함수 생성과 시간 함수로 클리어 시간 표시

버튼이 클릭된 시간을 구하기위해 datetime모듈을 import 해줍니다.   
```python
import datetime from datetime
```   
   

랜덤한 위치에 생성된 버튼을 제거하고 다른 새로운 버튼을 만드는 함수를 생성합니다.   
   
```python
def other_btn():
    global count
    # 카운트된 버튼의 숫자가 입력창에 입력한 숫자보다 작을 때
    if count < num_t:
        count += 1
        btn.destroy()
        ran_btn()
    else:  # 새로 버튼을 실행하지 않도록 설정
        final = datetime.now()  # 종료 시간
        dif_sec = (final-start).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text="Clear " + str(dif_sec)+"초")
        lab.pack(pady=230)
    # 버튼을 클릭했을 때 위젯을 모두 없애고 창크기를 키워주는 함수


def btn_f():
    global start
    global num_t  # num_t 변수를 전역변수로 지정
    num_t = int(ent.get())  # 입력창에 입력된 문자열을 숫자로 바꿔서 저장
    # 3개의 위젯이 요소로 있는 리스트 [label, entry, button]
    for widget in win.grid_slaves():
        widget.destroy()  # 위젯 요소를 차례로 파괴합니다.
    win.geometry("500x500")  # 창의 크기를 500x500로 설정합니다.
    ran_btn()
    start = datetime.now()  # 스타트 시간
```

스타트 시간과 종료 시간을 구해서 뺀 값을 total_seconds() 함수를 사용해서 간단하게 초를 구한뒤 clear 메시지 뒤에 넣어줬습니다.   

## 최종 코드와 프로그램 실사용 모습입니다.

다음은 최종 코드입니다.
```python
from tkinter import *
import random
from datetime import datetime
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
        final = datetime.now()  # 종료 시간
        dif_sec = (final-start).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text="Clear " + str(dif_sec)+"초")
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
    global start
    global num_t  # num_t 변수를 전역변수로 지정
    num_t = int(ent.get())  # 입력창에 입력된 문자열을 숫자로 바꿔서 저장
    # 3개의 위젯이 요소로 있는 리스트 [label, entry, button]
    for widget in win.grid_slaves():
        widget.destroy()  # 위젯 요소를 차례로 파괴합니다.
    win.geometry("500x500")  # 창의 크기를 500x500로 설정합니다.
    ran_btn()
    start = datetime.now()  # 스타트 시간


btn = Button(win)
btn.config(text="시작")
btn.config(command=btn_f)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()
```   
   
프로그램을 실행하면 다음과 같습니다.   
![aimgame_button](https://user-images.githubusercontent.com/58906858/152113789-3822ce82-1500-4238-a3af-e35bf2a54728.png)

표적 개수 입력창에 3을 입력하고 버튼을 누릅니다. 버튼이 3개가 랜덤한 위치에 생성되고 마지막으로 클리어 타임이 기록됩니다.




