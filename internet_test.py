import tkinter as tk
import webbrowser as web
roop_3=tk.Tk()
roop_3.geometry("450x350+100+100")
roop_3.resizable(False, False)
roop_3.title("internet")
def goggle():
    web.open("https://www.google.com/")#구글
def youtube():
    web.open("https://www.youtube.com/")#유튜브
def naver():
    web.open("https://www.naver.com/")#내이버

def calc(event):
    web.open(e.get())
e=tk.Entry(roop_3)
e.bind("<Return>", calc)
e.pack()
b_goggle=tk.Button(roop_3,overrelief="solid", width=9, command=goggle, repeatdelay=1000, repeatinterval=100, text="google")
b_goggle.pack()
b_youtube=tk.Button(roop_3,overrelief="solid", width=9, command=youtube, repeatdelay=1000, repeatinterval=100, text="youtube")
b_youtube.pack()
b_naver=tk.Button(roop_3,overrelief="solid", width=9, command=naver, repeatdelay=1000, repeatinterval=100, text="naver")
b_naver.pack()
roop_3.mainloop()