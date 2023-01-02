#tkinter로 화면에 띄우는 코드

from tkinter import *
import tkinter
import str_con as sc


window = Tk()
window.title("random_string")	# 윈도우창 이름
window.geometry("1000x300")	#크기 가로x세로


my_text =Text(window,font=20,height=4,width=700)

def on_click():
    my_text.delete("1.0", "end")
    my_text.insert('1.0',sc.rand_str())
    
btn = tkinter.Button(window,text = 'btn',background ='white', command=on_click)
btn.bind('f',on_click)


# 버튼 옵션설정
btn.config(width = 5, height = 2)
btn.config(text = "button")

# 버튼 배치하기
btn.pack()
my_text.pack()

window.mainloop()