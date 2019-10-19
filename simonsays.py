from tkinter import *
import random

root = Tk()

w = Canvas(root, width=400, height=400)
w.pack()

def default_colors():
    w.create_rectangle(0, 0, 200, 200, fill="red", tag='red')
    w.create_rectangle(200, 0, 400, 200, fill="blue", tag='blue')
    w.create_rectangle(0, 200, 200, 400, fill="yellow", tag='yellow')
    w.create_rectangle(200, 200, 400, 400, fill="green", tag='green')

default_colors()

colors = ['red', 'blue', 'yellow', 'green']
positions = {'red': (0, 0, 200, 200), 'blue': (200, 0, 400, 200), 'yellow': (0, 200, 200, 400), 'green': (200, 200, 400, 400)}


def showxy(event):
    '''
    show x, y coordinates of mouse click position
    event.x, event.y relative to ulc of widget (here root) 
    '''
    x1 = 0
    y1 = 0
    xy = 'rectangle x=%s  y=%s' % (event.x-x1, event.y-y1)
    root.title(xy) 

w.tag_bind('red', '<Button-1>', showxy)
w.tag_bind('green', '<Button-1>', showxy)
w.tag_bind('blue', '<Button-1>', showxy)
w.tag_bind('yellow', '<Button-1>', showxy)

light_colors = {'yellow': '#FBFF9E', 'red': '#FF7959', 'blue': '#95B4FF', 'green': '#95FFA0'}
seq = []
seq = ['blue', 'yellow','red','blue']

def task():
    default_colors()
    root.after(1000, task)  # reschedule event in 2 seconds
    color = random.choice(colors)
    position_tuple = positions[color]
    color = light_colors[color]
    w.create_rectangle(*position_tuple, fill=color)


root.after(1000, task)
mainloop()
