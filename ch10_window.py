from tkinter import *
window = Tk()
window.title('윈도우 창 연습')
#window.geometry('500x200')

label1 = Label(window, text = 'Cook Book Python을')
label2 = Label(window, text = '열심히', font = ('궁서체', 30, 'bold'), fg = 'red')
label3 = Label(window, text = '공부중입니다.', bg = 'magenta', width = 50, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

photo = PhotoImage(file = 'gif/dog.gif')
label4 = Label(window, image = photo)
label4.pack()

window.mainloop()
