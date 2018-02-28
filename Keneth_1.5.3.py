#####
# position_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter #often people import Tkinter as *

#####
# Create root window 
####
root = Tkinter.Tk()

#####
# Create Model
######
y_intvar = Tkinter.IntVar()
y_intvar.set(150) #initialize radius
# center of circle
x = 150 
r = 50

######
# Create Controller
#######
# Event handler for slider
def y_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    y = y_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
# Instantiate and place slider
position_changer = Tkinter.Scale(root, from_=1, to=150, variable=y_intvar,    
                              label='y coordinate', command=y_changed)
position_changer.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
y = y_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()

#####
# color_changer.py
# 
# Creates two Scales and a Text view. Updates Text based on the Scales
# 
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter # Often people import Tkinter as *

#####
# Create root window 
####
root = Tkinter.Tk()
root.wm_title('Hexadecimal Explorer')

#####
# Create Model
######
# Create two IntVar's and initialize them to 127
red_intvar = Tkinter.IntVar() 
red_intvar.set(127) 
green_intvar = Tkinter.IntVar()
green_intvar.set(127)
c_intvar = Tkinter.IntVar()
c_intvar.set(150)
x=150
y=150
r=100

######
# Create Controller
#######
# Event handler for slider
def color_changed(new_intval):
    # Controller updates the view by pulling data from model
    editor.insert(Tkinter.END, '#' + \
                               hexstring(red_intvar) + \
                               hexstring(green_intvar) + '00\n')
    editor.see(Tkinter.END) # scroll the Text window to see the new bottom line
    
# Instantiate and place sliders
red_slider = Tkinter.Scale(root, from_=0, to=255, variable=red_intvar, 
                           orient=Tkinter.HORIZONTAL,   
                           label='Red', command=color_changed)
red_slider.grid(row=1, column=0, sticky=Tkinter.E)
green_slider = Tkinter.Scale(root, from_=0, to=255, variable=green_intvar,  
                             orient=Tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=Tkinter.E)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=1, rowspan=1, column=1) 
                                
######
# Create View
#######
# Create a text editor window for displaying information
editor = Tkinter.Text(root, width=10)
editor.grid(column=2, row=0, rowspan=3)

######
# Function to convert IntVar data from Scale widget to two hex digits as string
# for a Canvas widget color argument
#######

def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a 2-character string representing a value in hexadecimal
    '''
    # Get an integer from an IntVar
    slider_int = slider_intvar.get()
    # Convert to hex
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits

c = c_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                outline='#000000', fill= 'yellow')
#######
# Event Loop
#######
root.mainloop()