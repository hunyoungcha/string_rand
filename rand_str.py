#keyword button

from tkinter import *
import tkinter


window = Tk()
window.title("random_string")	# 윈도우창 이름
window.geometry("1000x600")	#크기 가로x세로
window.resizable(width=FALSE, height=FALSE)	#리사이즈 가로세로 금지

btn = tkinter.Button(window,text = 'btn',background = 'white')

# 버튼 옵션설정
btn.config(width = 5, height = 2)
btn.config(text = "button")

# 버튼 배치하기
btn.pack()


window.mainloop()