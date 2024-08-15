# from tkinter import * 
# from PIL import Image,ImageTk 
# import math

# def getDigits(digit):
#     # # print(type(digit))
#     # print(digit)
#     # current = result_label['text']
#     # new_value = current + str(digit)
#     # # print(new_value)
#     # result_label.config(text=new_value)
#     # if digit=='C':
#     #     result_label.config(text='')
#         current = result_label['text']
    
#         if digit == 'C':
#             result_label.config(text='')
#             return
    
#         if digit == '=':
#             try:
#                 expression = current
#                 result = eval(expression)  
#                 result_label.config(text=str(result))
#             except ZeroDivisionError:
#                 result_label.config(text='Error')
#             except Exception as e:
#                 result_label.config(text='Error')
#             return
    
#         new_value = current + str(digit)
#         result_label.config(text=new_value)

# def scientificFunction(func):
#     current = result_label['text']
#     try:
#         result = eval(f"math.{func}({current})")
#         result_label.config(text=str(result))
#     except Exception as e:
#         result_label.config(text='Error')

# root = Tk()
# root.title('Calculator')
# root.geometry('320x500')
# root.resizable(0,0)
# root.config(background='black')

# # display section
# result_label = Label(root,text='',bg='black',fg='white')
# result_label.grid(row=0,column=0,columnspan=5,pady=(20,10),sticky='w')
# result_label.config(font=('verdana',12,'bold'))


# # button section
# # btn7 = Button(root,text='7',bg='gray',fg='black',width=3,height=1)
# # btn7.grid(row=1,column=0)
# # btn7.config(font=('verdana',12))

# # btn8 = Button(root,text='8',bg='gray',fg='black',width=3,height=1)
# # btn8.grid(row=1,column=1)
# # btn8.config(font=('verdana',12))

# # btn9 = Button(root,text='9',bg='gray',fg='black',width=3,height=1)
# # btn9.grid(row=1,column=2)
# # btn9.config(font=('verdana',12))

# # btnAdd = Button(root,text='+',bg='gray',fg='black',width=3,height=1)
# # btnAdd.grid(row=1,column=3)
# # btnAdd.config(font=('verdana',12))


# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
#     ('0', 4, 1), ('.', 4, 2), ('=', 4, 3), ('/', 4, 4),
    
#     ('C', 5, 0), ('sqrt', 5, 1), ('exp', 5, 2), ('(', 5, 3),
#     (')', 5, 4), ('log', 6, 0), ('ln', 6, 1), ('sin', 6, 2),
#     ('cos', 6, 3), ('tan', 6, 4)
# ]

# for (text,row,col) in buttons:
#     if text in ['sqrt', 'exp', 'log', 'ln', 'sin', 'cos', 'tan']:
#         Button(root, text=text, bg='gray', fg='black', width=6, height=2, font=('verdana', 12),
#                command=lambda text=text: scientificFunction(text)).grid(row=row, column=col, sticky='nsew')
        
#     else:
#         Button(root,text=text,bg='gray',fg='black',width=6,height=2,font=('verdana',12),command=lambda text=text:getDigits(text)).grid(row=row,column=col, sticky='nsew')
    
# for i in range(7):
#     root.grid_rowconfigure(i, weight=1)
# for i in range(5):
#     root.grid_columnconfigure(i, weight=1)
    
# root.mainloop()


# -------------------scientific version----------------------
from tkinter import *
import math
import os
def getDigits(digit):
    global last_was_result
    global last_result

    current = result_label['text']
    
    if digit == 'C':
        result_label.config(text='')
        last_was_result = False
        return
    
    if digit == '=':
        if last_was_result:
            # If the last operation was '=', do nothing
            return
        
        if not current.strip():
            # If the display is empty or contains only spaces, do nothing
            return
        
        try:
            expression = current
            result = eval(expression)
            result_label.config(text=str(result))
            last_result = result  # Store the last result
            last_was_result = True
        except ZeroDivisionError:
            result_label.config(text='Error')
            last_was_result = False
        except Exception as e:
            result_label.config(text='Error')
            last_was_result = False
        return
    
    # Clear the last result state if any other button is pressed
    new_value = current + str(digit)
    result_label.config(text=new_value)
    last_was_result = False

def scientificFunction(func):
    global last_was_result
    global last_result

    current = result_label['text']
    try:
        if not current.strip():
            # If the display is empty, do nothing
            return
        
        if func == 'π':
            result = math.pi
        elif func == 'ln':
            result = math.log(float(current))  # Natural logarithm
        elif func == 'sqrt':
            result = math.sqrt(float(current))
        elif func == '!':
            # Factorial function
            n = int(float(current))
            result = math.factorial(n)
        else:
            # Convert degrees to radians for trigonometric functions
            if func in ['sin', 'cos', 'tan']:
                current = math.radians(float(current))
            
            result = eval(f"math.{func}({current})")
        
        # Round the result to 10 decimal places for better precision
        result_label.config(text=f"{result:.10f}".rstrip('0').rstrip('.'))
        last_result = result  # Store the last result
        last_was_result = False
    except Exception as e:
        result_label.config(text='Error')
        last_was_result = False

def showLastResult():
    global last_result
    result_label.config(text=str(last_result))

root = Tk()
root.title('Calculator')
# root.iconbitmap('fav.ico')
root.geometry('400x600')
root.resizable(0,0)
root.config(background='black')

# Initialize global state
last_was_result = False
last_result = None  # Store the last result

# Display section
result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=5, pady=(20,10), sticky='w')
result_label.config(font=('verdana', 12, 'bold'))

# Button section
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('%', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('Ans', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('(', 3, 4),
    ('0', 4, 1), ('.', 4, 2), ('=', 4, 3), (')', 4, 4), ('!', 4, 0),
    
    ('C', 5, 0), ('sqrt', 5, 1), ('exp', 5, 2), ('(', 5, 3), (')', 5, 4),
    ('log', 6, 0), ('ln', 6, 1), ('sin', 6, 2), ('cos', 6, 3), ('tan', 6, 4),
]

for (text, row, col) in buttons:
    if text in ['sqrt', 'exp', 'log', 'ln', 'sin', 'cos', 'tan', '!']:
        Button(root, text=text, bg='gray', fg='black', width=6, height=2, font=('verdana', 12),
               command=lambda text=text: scientificFunction(text)).grid(row=row, column=col, sticky='nsew')
    elif text == 'Ans':
        Button(root, text=text, bg='gray', fg='black', width=6, height=2, font=('verdana', 12),
               command=showLastResult).grid(row=row, column=col, sticky='nsew')
    else:
        Button(root, text=text, bg='gray', fg='black', width=6, height=2, font=('verdana', 12),
               command=lambda text=text: getDigits(text)).grid(row=row, column=col, sticky='nsew')

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()


