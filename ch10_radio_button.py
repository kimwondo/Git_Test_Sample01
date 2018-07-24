from tkinter import *
window = Tk()

def myFunc():
  if var.get() == 1:
    label1.configure(text = '파이썬')
  elif var.get() == 2:
    label1.configure(text = 'C++')
  else:
    label1.configure(text = 'Java')
    # widjet.configure(옵션=값)은 해당 위젯의 옵션값을 변경시켜 주는 함수이다.

var = IntVar()
rb1 = Radiobutton(window, text = '파이썬', variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = 'C++', variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = 'Java', variable = var, value = 3, command = myFunc)

label1 = Label(window, text = '선택한 언어', fg = 'magenta')

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()

