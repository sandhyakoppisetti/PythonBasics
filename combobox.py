import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
root=tk.Tk()
root.title("scrolledtest")
root.geometry("700x700")

ttk.Label(root,text="python life",background="blue",foreground="white",font=("Times new Roman",15 )).grid(row=0,column=1)

'''#combobox
n=tk.StringVar()
course=ttk.Combobox(root,width=20,textvariable=n)
course['values']=("Pythoon",
                    "django",
                    "machinelearning")
course.grid(column=1,row=5)
course.current()'''
#scrolledtext
text1=scrolledtext.ScrolledText(root,wrap=tk.WORD,width= 40, height=10)
text1.grid(column=0,padx=10,pady=10)
text1.focus()
root.mainloop()
