from tkinter import *
window = Tk()

btnList = [None]*3

for i in range(0, 3):
  btnList[i] = Button(window, text = 'Button' + str(i + 1), command = quit)

for btn in btnList:
  btn.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 5, pady = 5)

window.mainloop()
