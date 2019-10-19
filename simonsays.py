from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

w.create_rectangle(0, 0, 200, 200, fill="red", tag='red')
w.create_rectangle(200, 0, 400, 200, fill="blue", tag='blue')
w.create_rectangle(0, 200, 200, 400, fill="yellow", tag='yellow')
w.create_rectangle(200, 200, 400, 400, fill="green", tag='green')

print(master.winfo_pointerxy())

def showxy(event):
    '''
    show x, y coordinates of mouse click position
    event.x, event.y relative to ulc of widget (here root) 
    '''
    # xy relative to ulc of root
    #xy = 'root x=%s  y=%s' % (event.x, event.y)
    # optional xy relative to blue rectangle
    x1 = 0
    y1 = 0
    xy = 'rectangle x=%s  y=%s' % (event.x-x1, event.y-y1)
    master.title(xy) 

w.tag_bind('red', '<Button-1>', showxy)
w.tag_bind('green', '<Button-1>', showxy)
w.tag_bind('blue', '<Button-1>', showxy)
w.tag_bind('yellow', '<Button-1>', showxy)
mainloop()
