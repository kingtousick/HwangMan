from tkinter import *

def change_state():
    global sw

    if sw:
        lbl['state']='active'
    else:
         lbl['state'] = 'disable'
    sw= not sw
def from_set():
    global lbl
    win=Tk()
    win.title("최강 롯데정보통신")
    win.geometry("300x100")
    lbl=Label(win,
              text='안녕 롯데',
              font='궁서 40',
              state='active',
              activeforeground='red',
              disabledforeground='blue')
    lbl.pack()
    btn=Button(win, text="충성하기", command= change_state)
    btn.pack()
    return win
if __name__ =='__main__':
    sw=False
    mas=from_set()
    mas.mainloop()