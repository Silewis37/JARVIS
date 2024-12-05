# File Name: GUI-Test.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[*] Work on Getting the main basics of the GUI setup and make sure that it works in a basic environment
#[] Work on Getting the main basics of the GUI's custom keyboard setup and make sure that it works and can be changed into multiple different keyboard layouts and make it seem less.
#[] Work on Getting the basics of handTracking in the GUI and the way the GUI can be treated using the hand Tracking
#[] Work on Getting the HandTracking to a point where the GUI can not be affected or moved around and is only bound to the board.

#* Libraries *#

import tkinter as tk

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

klavesnice = tk.Tk()
klavesnice.geometry("800x700+120+100")

buttons = [
    'q','w','e','r','t','y','u','i','o','p',
    'a','s','d','f','g','h','j','k','l',
    'z','x','c','v','b','n','m'
]

zadane = ''
entry = tk.Text(klavesnice, width=43, height=3)
entry.grid(row=1, columnspan=40)


radek = 3 #row
sloupec = 0 #column

#& Functions &#

def select(value):
    global zadane
    if value == 'Space':
        entry.insert('end', ' ')
    else:
        entry.insert('end', value)
        zadane = zadane + value
        print(f'{zadane=!r}')


#= Classes =#

#~ define and build classes here

#! Main Program !#

for button in buttons:
    command = lambda x=button: select(x)
    if button != 'Space':
        tk.Button(klavesnice, text=button, width=5, font=("arial", 14, "bold"),
                  bg='powder blue', command=command, padx=3.5, pady=3.5, bd=5
                 ).grid(row=radek, column=sloupec)
    if button == 'Space':
        tk.Button(klavesnice, text=button, command=command).grid(row=5, column=sloupec)
    sloupec += 1
    # Specify the keyboard layout
    if sloupec > 9 and radek == 3:
        sloupec = 0
        radek += 1
    if sloupec > 8 and radek == 4:
        sloupec = 0
        radek += 1

klavesnice.mainloop()




#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#