from tkinter import *
from tkinter import messagebox

# 함수 선언
def keyEvent(event):
  txt = '눌린 키 : shift + '
  if event.keycode == 37:
    txt += '왼쪽 화살표'
  elif event.keycode == 38:
    txt += '위쪽 화살표'
  elif event.keycode == 39:
    txt += '오른쪽 화살표'
  elif event.keycode == 40:
    txt += '아래쪽 화살표'  
  messagebox.showinfo('키보드 이벤트', txt)

# Main Code
window = Tk()
window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()

