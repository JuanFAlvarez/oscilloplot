import tkinter as tk
# prints raw x and y to be processed

X = []
Y = []
lastx, lasty = 0, 0

# xy and addLine are for graphical purposes only
# on_move_press is the one that logs the one to the list and fixes Y

def xy(event):
    # logs coordinates when mouse is clicked
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    # draws line from old point to new point
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y

# logs clicked coordinate on list
def on_move_press( event):
    curX, curY = (event.x, event.y)
    curY=255-curY
    X.append(str(curX))
    Y.append(str(curY))

# set up needed for window
root = tk.Tk()
root.geometry("255x255")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# bind left click and drag to functions and start loop
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
root.bind("<B1-Motion>",on_move_press)
root.mainloop()

print("const int NUM_POINTS = %s;" % str(len(X)))
print("const unsigned long x_points[NUM_POINTS] = {%s};" % ','.join(X))
print("const unsigned long y_points[NUM_POINTS] = {%s};" % ','.join(Y))

#call python drawlog.py > arduino_list.txt
