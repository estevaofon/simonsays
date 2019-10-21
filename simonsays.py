import tkinter
import random
import time

root = tkinter.Tk()

w = tkinter.Canvas(root, width=400, height=400)
w.pack()
colors_clicked = []

def default_colors():
    w.create_rectangle(0, 0, 200, 200, fill="green", tag='green')
    w.create_rectangle(200, 0, 400, 200, fill="red", tag='red')
    w.create_rectangle(0, 200, 200, 400, fill="yellow", tag='yellow')
    w.create_rectangle(200, 200, 400, 400, fill="blue", tag='blue')

default_colors()

def showxy(event):
    '''
    show x, y coordinates of mouse click position
    event.x, event.y relative to ulc of widget (here root) 
    '''
    x1 = 0
    y1 = 0
    x = event.x-x1
    y = event.y-y1
    message = 'rectangle x=%s  y=%s' % (x, y)
    if x < 200 and y <200: 
        message = 'green'
    elif x > 200 and y <200: 
        message = 'red'
    elif x < 200 and y > 200: 
        message = 'yellow'
    else:
        message = 'blue'
    colors_clicked.append(message)
    print(colors_clicked)
    light_rect(message)
    w.update()
    time.sleep(0.3)
    w.update()
    default_colors()

    root.title(message) 

w.tag_bind('red', '<Button-1>', showxy)
w.tag_bind('green', '<Button-1>', showxy)
w.tag_bind('blue', '<Button-1>', showxy)
w.tag_bind('yellow', '<Button-1>', showxy)

colors = ['red', 'blue', 'yellow', 'green']
positions = {'green': (0, 0, 200, 200), 'red': (200, 0, 400, 200), 'yellow': (0, 200, 200, 400), 'blue': (200, 200, 400, 400)}
light_colors = {'yellow': '#FBFF9E', 'red': '#FF7959', 'blue': '#95B4FF', 'green': '#95FFA0'}
seq = []
delta_time = 1000 

def light_rect(color):
    position_tuple = positions[color]
    light_color = light_colors[color]
    w.create_rectangle(*position_tuple, fill=light_color)

def paint_color():
    for color in seq:
        position_tuple = positions[color]
        light_color = light_colors[color]
        w.create_rectangle(*position_tuple, fill=light_color)
        time.sleep(0.5)
        w.update()
        time.sleep(1)
        default_colors()
        w.update()


def task():
    default_colors()
    color = random.choice(colors)
    seq.append(color)
    paint_color()
    global colors_clicked
    colors_clicked = []
    root.after(1000, clean_colors)

def clean_colors():
    default_colors()
    global delta_time
    delta_time += 1000
    root.after(delta_time, check)

def restart():
    global delta_time
    delta_time = 1000
    global seq
    seq = []

def check():
    if seq == colors_clicked:
        print("Acertou!")
    else:
        print("errou")
        global colors
        for i in range(3):
            for color in colors:
                light_rect(color)
            w.update()
            time.sleep(0.5)
            default_colors()
            w.update()
            time.sleep(0.5)
        restart()
    root.after(1000, task)


root.after(1000, task)
tkinter.mainloop()