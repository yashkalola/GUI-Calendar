from tkinter import *

from tkcalendar import Calendar

root = Tk()
root.title("Calendar")
root.geometry("400x400")

cal = Calendar(root, selectmode = 'day', firstweekday = "sunday", date_pattern = "dd-mm-yyyy", background = "black", headersbackground = "white", selectbackground = "black", selectforeground = "white")
cal.pack(pady = 20)

def grad_date():
	date.config(text = "Selected Date is : " + cal.get_date())

Button(root, text = "Select the Date", command = grad_date).pack(pady = 20)
date = Label(root, text = "")
date.pack(pady = 20)

root.mainloop()
