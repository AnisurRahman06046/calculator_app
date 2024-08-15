from tkinter import *
import math

def getDigits(digit):
    global last_was_result

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

# def scientificFunction(func):
#     global last_was_result
#     current = result_label['text']
#     try:
#         if not current.strip():
#             # If the display is empty, do nothing
#             return
        
#         result = eval(f"math.{func}({current})")
#         result_label.config(text=str(result))
#         last_was_result = False
#     except Exception as e:
#         result_label.config(text='Error')
#         last_was_result = False
# def scientificFunction(func):
#     global last_was_result
#     current = result_label['text']
#     try:
#         if not current.strip():
#             # If the display is empty, do nothing
#             return
        
#         # Convert degrees to radians for trigonometric functions
#         if func in ['sin', 'cos', 'tan']:
#             # Convert input from degrees to radians
#             current = math.radians(float(current))
        
#         result = eval(f"math.{func}({current})")
#         # Round the result to 10 decimal places for better precision
#         result_label.config(text=f"{result:.10f}".rstrip('0').rstrip('.'))
#         last_was_result = False
#     except Exception as e:
#         result_label.config(text='Error')
#         last_was_result = False
def scientificFunction(func):
    global last_was_result
    current = result_label['text']
    try:
        if not current.strip():
            # If the display is empty, do nothing
            return
        
        if func == 'π':
            result = math.pi
        elif func == 'ln':
            result = math.log(float(current))  # Natural logarithm
        elif func == 'e':
            result = math.e
        else:
            # Convert degrees to radians for trigonometric functions
            if func in ['sin', 'cos', 'tan']:
                current = math.radians(float(current))
            
            result = eval(f"math.{func}({current})")
        
        # Round the result to 10 decimal places for better precision
        result_label.config(text=f"{result:.10f}".rstrip('0').rstrip('.'))
        last_was_result = False
    except Exception as e:
        result_label.config(text='Error')
        last_was_result = False
root = Tk()
root.title('Calculator')
root.iconbitmap('fav.ico')
root.geometry('400x600')
root.resizable(0,0)
root.config(background='black')

# Initialize global state
last_was_result = False

# display section
result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=5, pady=(20,10), sticky='w')
result_label.config(font=('verdana', 12, 'bold'))

# button section
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('%', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('√', 3, 4),
    ('0', 4, 1), ('.', 4, 2), ('=', 4, 3), ('/', 4, 4), ('π', 4, 0),
    
    ('C', 5, 0), ('sqrt', 5, 1), ('exp', 5, 2), ('(', 5, 3), (')', 5, 4),
    ('log', 6, 0), ('ln', 6, 1), ('sin', 6, 2), ('cos', 6, 3), ('tan', 6, 4),
    ('!', 7, 0), ('e', 7, 1), ('abs', 7, 2), ('floor', 7, 3), ('ceil', 7, 4)
]

for (text, row, col) in buttons:
    if text in ['sqrt', 'exp', 'log', 'ln', 'sin', 'cos', 'tan', '!', 'abs', 'floor', 'ceil']:
        Button(root, text=text, bg='gray', fg='black', width=6, height=2, font=('verdana', 12),
               command=lambda text=text: scientificFunction(text)).grid(row=row, column=col, sticky='nsew')
    else:
        Button(root, text=text, bg='gray', fg='black', width=6, height=2, font=('verdana', 12),
               command=lambda text=text: getDigits(text)).grid(row=row, column=col, sticky='nsew')

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()