#Importing the library
from tkinter import *
while 1:
	#Create an instance of tkinter window or frame
	win= Tk()

	#Setting the geometry of window
	win.geometry("600x600")
	win.overrideredirect(1)
	#Create a Label
	Label(win, text= '''


░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▒▒▒▒▒░░░░░░▒▒░░░░▒▓▓▓▒░░░░░░░░░░░░░
░░░░░░░░░░▒▒▒▒▒░░░░░░░▒░░░░▓▓▓▓▓░░░░░░░░░░░░░
░░░░░░░░░░░░░▒▒▒░░░▒▒▒▒▒▒▒▒▓▓▓▒▒░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░
░░░░░░▒▒▒▒░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒░░░▒▒▒▒▒░░░░░░░
░░░░░░▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░
░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒▒▒▒▒░░▒▒░░░▒▒▒▒▒░░░░░░░░░░░░░░
░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒░░▒▒▒▒▒▒▒░░░░░░
░░░░░░░▒▒▒▒▒▒░░░░▓▒▒▒▒▒▒▒▒▒▓▓░░░░░▒▒▒▒▒░░░░░░
░░░░░░░░░░░░░░░░▒▓▒░░░▒▒▒░░▓▓▒▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░▒▓▓▓░░░░░░▒▒░░▓▓▓▓▓░░░░░░░░░░░░░
░░░░░░░░░░░░░▓▓▓▒░░░░░▒▒▒░░▒▓▓▓▓░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


''',font=('Helvetica bold', 12)).pack(pady=20)

	#Make the window jump above all
	win.attributes('-topmost',True)

	win.mainloop()
