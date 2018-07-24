from tkinter import *
from tkinter import messagebox

# 함수 선언
def myFunc():
  messagebox.showinfo('강아지 버튼', '강아지가 귀엽지요?')

# Main Code
window = Tk()
window.title('Window PhotoImage')

photo1 = PhotoImage(file = 'gif/dog2.gif')
photo2 = PhotoImage(file = 'gif/cat2.gif')
photo3 = PhotoImage(file = 'gif/dog6.gif')

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

button1 = Button(window, text = 'Python Exit', fg = 'red', command = quit)
button1.pack(side=BOTTOM)

button2 = Button(window, image = photo3, command = myFunc)
button2.pack(side=LEFT)

window.mainloop()
