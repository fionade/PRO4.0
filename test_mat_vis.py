#Trying to visualise center of mass of four inputs using Tkinter
#Will be used for the weight sensor mat

import Tkinter
root = Tkinter.Tk()

def move_dot():
    #Meh..
    global last_center_x
    global last_center_y

    var0 = scale0.get()
    var1 = scale1.get()
    var2 = scale2.get()
    var3 = scale3.get()

    #Initialize center of mass in case sum of weights is zero
    center_of_mass_x = canvas_width  / 2
    center_of_mass_y = canvas_height / 2

    sum_weights = var0 + var1 + var2 + var3

    if sum_weights > 0:
        center_of_mass_x = int( canvas_width *  (var1+var3) / sum_weights)
        center_of_mass_y = int( canvas_height * (var2+var3) / sum_weights)

    #canvas.move only takes offsets
    offset_x = center_of_mass_x - last_center_x
    offset_y = center_of_mass_y - last_center_y

    last_center_x = center_of_mass_x
    last_center_y = center_of_mass_y

    print("Offset: x= " + str(offset_x) + " y= " + str(offset_y))

    canvas.move("dot", offset_x, offset_y)

def init():
    x = canvas_width / 2
    y = canvas_height / 2
    r = 2
    dot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", tags="dot")

canvas_height = 300
canvas_width  = 400

canvas = Tkinter.Canvas(root, bg="white", height=canvas_height, width=canvas_width)
canvas.grid(row=1, rowspan=4, column=1, columnspan=4)

#To-Do: convert the following blocks to loop
scale0 = Tkinter.Scale(root)
scale1 = Tkinter.Scale(root)
scale2 = Tkinter.Scale(root)
scale3 = Tkinter.Scale(root)

scale0.grid(row=1, column=0, rowspan=2)
scale1.grid(row=1, column=6, rowspan=2)
scale2.grid(row=3, column=0, rowspan=2)
scale3.grid(row=3, column=6, rowspan=2)

#Move dot button
button = Tkinter.Button(root, text='Move', command=move_dot)
button.grid(row = 0, column=0, columnspan=6)

#Init code
x = canvas_width / 2
y = canvas_height / 2
r = 2
dot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", tags="dot")
last_center_x = x
last_center_y = y

root.mainloop()