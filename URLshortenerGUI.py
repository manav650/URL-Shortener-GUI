from pyshorteners import *
from tkinter import *
from tkinter import messagebox
from pyshorteners.exceptions import BadURLException

def urlShortener():
    try:
        num2.delete(0,END)
        url = Shortener()
        url_name = num1.get()
        short_url = url.tinyurl.short(url_name)
        num2.insert(0,short_url)
        num1.clipboard_clear()
        
    except BadURLException:
        messagebox.showerror("Error!", "No URL Received\nTry again")
    
    
    
def clear():
    num1.delete(0,END)
    num2.delete(0,END)
    
    
def copy_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(num2.get())
    clip.destroy()


win = Tk()
win.title("URL Shortener")
font_format = ("Helvetica",15,"bold")

label1 = Label(win,text="Enter Url to shorten",font=font_format)
label2 = Label(win,text="Shortened Url",font=font_format)

num1 = Entry(win,width=50)
num2 = Entry(win,width=50)

button1 = Button(win,text="Shorten",padx=30,pady=5,command=urlShortener)
button2 = Button(win,text="Clear",padx=30,pady=5,command=clear)
button3 = Button(win,text="Copy to Clipboard",padx=30,pady=5,command=copy_button)
button4 = Button(win,text="Exit",padx=30,pady=5,command=win.quit)


label1.grid(row=0,column=1)
num1.grid(row=1, column=1, ipadx=20, ipady=10)

button1.grid(row=2, column=1)
button2.grid(row=3, column=1)

label2.grid(row=4, column=1)
num2.grid(row=5, column=1, ipadx=20, ipady=10)

button3.grid(row=6, column=1)
button4.grid(row=7, column=1)

win.mainloop()