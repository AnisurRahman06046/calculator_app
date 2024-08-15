from tkinter import * 
from PIL import Image,ImageTk 

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
# root.config(background='black')

# display section
display = Label(root,text=0,bg='gray',fg='white')
display.grid(row=0,column=0,pady=(50,25))
display.config(font=('verdana',30,'bold'))

root.mainloop()