from tkinter import *
import win32gui
import time
from PIL import ImageGrab


WIN = Tk()
WIDHT = 5
COLOR='black'
BRUSH_WIDTH = DoubleVar(WIN)

WIN.title('Paint app -thelegitprogrammer')
def paint(event):
    x, y = event.x, event.y

    canvas.create_oval(x-WIDHT, y-WIDHT, x+WIDHT, y+WIDHT, fill=COLOR, width=0)

def setColor(newColor):
    global COLOR
    COLOR = newColor

def colorPallet():
    id = canvas2.create_rectangle(10, 10, 30, 30, fill='blue', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('blue'))
    id = canvas2.create_rectangle(40, 10, 60, 30, fill='black', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('black'))
    id = canvas2.create_rectangle(70, 10, 90, 30, fill='white', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('white'))
    id = canvas2.create_rectangle(100, 10, 120, 30, fill='purple', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('purple'))
    id = canvas2.create_rectangle(130, 10, 150, 30, fill='red', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('red'))
    id = canvas2.create_rectangle(160, 10, 180, 30, fill='orange', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('orange'))
    id = canvas2.create_rectangle(190, 10, 210, 30, fill='yellow', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('yellow'))
    id = canvas2.create_rectangle(220, 10, 240, 30, fill='brown4', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('brown4'))
    id = canvas2.create_rectangle(250, 10, 270, 30, fill='grey', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('grey'))
    id = canvas2.create_rectangle(280, 10, 300, 30, fill='green', width=1)
    canvas2.tag_bind(id, '<Button-1>', lambda x: setColor('green'))

def clear():
    canvas.delete('all')

def saveImage():
    id = canvas.winfo_id()
    rect = win32gui.GetWindowRect(id)
    currentTime = time.strftime('%S %M %S %p')
    ImageGrab.grab(rect).save(f"{currentTime}.png")
    canvas.delete('all')

def change_width(event):
    global WIDHT
    WIDHT = BRUSH_WIDTH.get()


canvas = Canvas(WIN, height=400, width=600, bg='white')
canvas2 = Canvas(WIN, height=40, width=600, bg='white')
button = Button(WIN, text='Clear All', command=clear)
button_save = Button(WIN, text='Save', command=saveImage)
scale = Scale(WIN, from_= 1, to = 50, variable = BRUSH_WIDTH, command = change_width, orient=HORIZONTAL)
canvas.bind("<B1-Motion>", paint)

canvas.pack()
canvas2.pack()
colorPallet()
button.pack()
button_save.pack()
scale.pack()
WIN.mainloop()