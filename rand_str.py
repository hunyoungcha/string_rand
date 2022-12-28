#keyword button

from tkinter import *
import tkinter
import random

window = Tk()
window.title("random_string")	# 윈도우창 이름
window.geometry("1000x300")	#크기 가로x세로

text=tkinter.Text(window)
text.config(width=800, height=5, font=10)

def on_click():
    #bg_ser에서 만든 리스트 받아와서 random 함수로 한개 들고 오기

btn = tkinter.Button(window,text = 'btn',background ='white', command=)

# 버튼 옵션설정
btn.config(width = 5, height = 2)
btn.config(text = "button")

# 버튼 배치하기
btn.pack()
text.pack()


window.mainloop()