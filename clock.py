
import time
from tkinter import *

def clock_main(): 
   live_T_mian = time.strftime("%H:%M:%S") 
   clock_width_main.config(text=live_T_mian)
   clock_width_main.after(200, clock_main) 

root_2 = Tk()
root_2.title("clock_main")
root_2.geometry("-1-1")
root_2.wm_attributes("-topmost", 1) 
txt_frame = Frame(root_2)
txt_frame.pack()

txt_width = Label(txt_frame, text="This time")
txt_width.pack()

clock_frame_main = Frame(root_2)
clock_frame_main.pack()

clock_width_main = Label(clock_frame_main, font=("Times",24,"bold"), bg="white", bd=8)
clock_width_main.pack()

clock_main()
root_2.mainloop()
