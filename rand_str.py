#keyword button

from tkinter import *
import tkinter
import str_con as sc


window = Tk()
window.title("random_string")	# 윈도우창 이름
window.geometry("1000x300")	#크기 가로x세로


def on_click():
    my_label.config(text = sc.rand_str())
    

btn = tkinter.Button(window,text = 'btn',background ='white', command=on_click)
my_label = Label(window)


# 버튼 옵션설정
btn.config(width = 5, height = 2)
btn.config(text = "button")

# 버튼 배치하기
btn.pack()
my_label.pack()

window.mainloop()