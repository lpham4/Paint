from tkinter import *
from tkinter import ttk

def comboShape(event):
    return val2.get()
def comboThick(event):
    return val3.get()
def radio():
    return val1.get()
def drawCurve(event):
    thick = val3.get()
    color = radio()
    shape = val2.get()
    if shape == "Curve" and thick == "Thin":
        if color == 1:
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            c = canvas.create_oval(x1, y1, x2, y2, outline = "mediumpurple1", width = 1)
        if color == 2:
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            c = canvas.create_oval(x1, y1, x2, y2, outline = "royalblue1", width = 1)
        if color == 3:
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            c = canvas.create_oval(x1, y1, x2, y2, outline = "orangered", width = 1)
    if shape == "Curve" and thick == "Thick":
        if color == 1:
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            c = canvas.create_oval(x1, y1, x2, y2, outline = "mediumpurple1", width = 3)
        if color == 2:
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            c = canvas.create_oval(x1, y1, x2, y2, outline = "royalblue1", width = 3)
        if color == 3:
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            c = canvas.create_oval(x1, y1, x2, y2, outline = "orangered", width = 3)

def draw(event3):
    shape = val2.get()
    color = radio()
    thick = val3.get()
    if shape == "Rectangle" and thick == "Thin":
        if color == 1:
            x, y = event3.x, event3.y
            c = canvas.create_rectangle(x, y, 50, 50, fill = "mediumpurple1", width = 1)
        if color == 2:
            x, y = event3.x, event3.y
            c = canvas.create_rectangle(x, y, 50, 50, fill = "royalblue1", width = 1)
        if color == 3:
            x, y = event3.x, event3.y
            c = canvas.create_rectangle(x, y, 50, 50, fill = "orangered", width = 1)
    if shape == "Rectangle" and thick == "Thick":
        if color == 1:
            x, y = event3.x, event3.y
            c = canvas.create_rectangle(x, y, 50, 50, fill = "mediumpurple1", width = 3)
        if color == 2:
            x, y = event3.x, event3.y
            c = canvas.create_rectangle(x, y, 50, 50, fill = "royalblue1", width = 3)
        if color == 3:
            x, y = event3.x, event3.y
            c = canvas.create_rectangle(x, y, 50, 50, fill = "orangered", width = 3)
    if shape == "Oval" and thick == "Thin":
        if color == 1:
            x, y = event3.x, event3.y
            c = canvas.create_oval(x, y, 50, 50, fill = "mediumpurple1", width = 1)
        if color == 2:
            x, y = event3.x, event3.y
            c = canvas.create_oval(x, y, 50, 50, fill = "royalblue1", width = 1)
        if color == 3:
            x, y = event3.x, event3.y
            c = canvas.create_oval(x, y, 50, 50, fill = "orangered", width = 1)
    if shape == "Oval" and thick == "Thick":
        if color == 1:
            x, y = event3.x, event3.y
            c = canvas.create_oval(x, y, 50, 50, fill = "mediumpurple1", width = 3)
        if color == 2:
            x, y = event3.x, event3.y
            c = canvas.create_oval(x, y, 50, 50, fill = "royalblue1", width = 3)
        if color == 3:
            x, y = event3.x, event3.y
            c = canvas.create_oval(x, y, 50, 50, fill = "orangered", width = 3)

def clear():
    canvas.delete("all")

root = Tk()
root.title("Paint")
root.geometry("700x400")

val1 = IntVar()
val2 = StringVar()
val3 = StringVar()

canvas = Canvas(root, width = 450, height = 350, borderwidth = 1, relief = "raised")
canvas.pack(side = "right")
canvas.bind("<B1-Motion>", drawCurve)
canvas.bind("<ButtonRelease-1>", draw)


combo1 = ttk.Combobox(root, values = ["Rectangle", "Oval", "Curve"], state = "readonly", textvariable = val2)
combo1.set("Choose Shape")
combo1.bind("<<ComboboxSelected>>", comboShape)
combo1.pack(side = "top")
combo2 = ttk.Combobox(root, values = ["Thin", "Thick"], state = "readonly", textvariable = val3)
combo2.set("Choose Thickness")
combo2.bind("<<ComboboxSelected>>", comboThick)
combo2.pack(side = "top")

button1 = Radiobutton(root, text = "Purple", variable = val1, value = 1,command = radio)
button1.pack(side = "top")
button2 = Radiobutton(root, text = "Blue", variable = val1, value = 2, command = radio)
button2.pack(side = "top")
button3 = Radiobutton(root, text = "Orange", variable = val1, value = 3, command = radio)
button3.pack(side = "top")
button5 = Button(root, text = "Clear", command = clear)
button5.pack(side = "top")

root.mainloop()