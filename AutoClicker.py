from time import sleep
from tkinter import *
import pyautogui as pg
import keyboard

select = 100
top = Tk()
options = [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2, 0.1 , 0.09 , 0.08 , 0.07 , 0.06 , 0.05 , 0.04 , 0.03 , 0.02 , 0.01 ]
  
clicked = StringVar()

def callback(selection):
    global select
    select = selection
    

clicked.set( "1" )

drop = OptionMenu( top , clicked , *options, command=callback)
drop.pack()
  
def start():
    x = 1
    startbtn.config(text="F2 to stop")
    while x == 1:
        print(select)
        pg.click()
        sleep(select)
        if keyboard.is_pressed('q'):
            startbtn.config(text="Start")
            print("stop")
            x = 0

startbtn = Button(top, text ="start", command=start)


startbtn.pack()
top.mainloop()
