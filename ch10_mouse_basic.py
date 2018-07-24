from tkinter import *
from tkinter import messagebox

# 함수선언
def clickImage(event):
  messagebox.showinfo('마우스', '토끼에서 마우스가 클릭됨')

# Main Code
window = Tk()
window.geometry('400x400')

photo = PhotoImage(file = 'gif/rabbit.gif')
label1 = Label(window, image = photo)

label1.bind('<Button>', clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()

