from tkinter import * 
from PIL import Image,ImageTk 


def getDigits(digit):
    # # print(type(digit))
    # print(digit)
    # current = result_label['text']
    # new_value = current + str(digit)
    # # print(new_value)
    # result_label.config(text=new_value)
    # if digit=='C':
    #     result_label.config(text='')
        current = result_label['text']
    
        if digit == 'C':
            result_label.config(text='')
            return
    
        if digit == '=':
            try:
                expression = current
                result = eval(expression)  
                result_label.config(text=str(result))
            except ZeroDivisionError:
                result_label.config(text='Error')
            except Exception as e:
                result_label.config(text='Error')
            return
    
        new_value = current + str(digit)
        result_label.config(text=new_value)

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.config(background='black')

# display section
result_label = Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
result_label.config(font=('verdana',12,'bold'))


# button section
# btn7 = Button(root,text='7',bg='gray',fg='black',width=3,height=1)
# btn7.grid(row=1,column=0)
# btn7.config(font=('verdana',12))

# btn8 = Button(root,text='8',bg='gray',fg='black',width=3,height=1)
# btn8.grid(row=1,column=1)
# btn8.config(font=('verdana',12))

# btn9 = Button(root,text='9',bg='gray',fg='black',width=3,height=1)
# btn9.grid(row=1,column=2)
# btn9.config(font=('verdana',12))

# btnAdd = Button(root,text='+',bg='gray',fg='black',width=3,height=1)
# btnAdd.grid(row=1,column=3)
# btnAdd.config(font=('verdana',12))


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text,row,col) in buttons:
    Button(root,text=text,bg='gray',fg='black',width=5,height=2,font=('verdana',14),command=lambda text=text:getDigits(text)).grid(row=row,column=col, sticky='nsew')
    
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    
root.mainloop()