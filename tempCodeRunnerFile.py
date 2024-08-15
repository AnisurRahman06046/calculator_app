for (text,row,col) in buttons:
    Button(root,text=text,bg='gray',fg='black',width=3,height=1,font=('verdana',12)).grid(row=row,column=col)