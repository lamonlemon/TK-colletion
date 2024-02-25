import tkinter as tk
import tkinter.colorchooser as tkcolor
import tkinter.simpledialog as tkdialg

def mouseClick(event):
    global x1,x2,y1,y2
    x1=event.x
    y1=event.y


def mouseDrop(event):
    global x1,x2,y1,y2,penWidth,penColor
    x2=event.x
    y2=event.y
    canvas.create_line(x1,y1,x2,y2, width=penWidth, fill=penColor)

def getColor():
    global penColor
    color=tkcolor.askcolor()
    penColor=color[1]

def getWidth():
    global penWidth
    penWidth=tkdialg.askinteger("line's whigth", "put number of line(1~10)",minvalue=1,maxvalue=10)

root=None
canvas=None
x1=x2=y1=y2=None
penColor="black"
penWidth=5

if __name__=="__main__":
    root=tk.Tk()
    canvas=tk.Canvas(root,height=300,width=300)
    canvas.bind("<Button-1>",mouseClick)
    canvas.bind("<ButtonRelease-1>",mouseDrop)
    canvas.pack()

    mainMenu=tk.Menu(root)
    root.config(menu=mainMenu)
    fileMenu=tk.Menu(mainMenu)
    mainMenu.add_cascade(label="seting",menu=fileMenu)
    fileMenu.add_command(label="line color",command=getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label="line width",command=getWidth)

    root.mainloop()