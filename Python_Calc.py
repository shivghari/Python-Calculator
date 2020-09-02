# PyhonCalc Using tkinter
# limitations :  cant use multiple operator in one line 
from tkinter import *
root = Tk()

data = StringVar()
new = ''

# Intermidiate variable 
a = 0

def one_clicked():
    global new
    global data
    new = new + '1'
    data.set(new)

def two_clicked():
    global new
    global data
    new = new + '2'
    data.set(new)
    
def three_clicked():
    global new
    global data
    new = new + '3'
    data.set(new)
    
def plus_clicked():
    global new
    global data
    new = new + '+'
    data.set(new)

def four_clicked():
    global new
    global data
    new = new + '4'
    data.set(new)
    
def five_clicked():
    global new
    global data
    new = new + '5'
    data.set(new)
    
def six_clicked():
    global new
    global data
    new = new + '6'
    data.set(new)
    
def minus_clicked():
    global new
    global data
    new = new + '-'
    data.set(new)
    
def seven_clicked():
    global new
    global data
    new = new + '7'
    data.set(new)

def eight_clicked():
    global new
    global data
    new = new + '8'
    data.set(new)

def nine_clicked():
    global new
    global data
    new = new + '9'
    data.set(new)    
    
def multiple_clicked():
    global new
    global data
    new = new + '*'
    data.set(new)
       
def C_clicked():
    global new
    global data
    new = ''
    data.set(new)

def zero_clicked():
    global new
    global data
    new = new + '0'
    data.set(new)
    
def divide_clicked():
    global new
    global data
    new = new + '/'
    data.set(new)
    
def equal_clicked():
    global new
    global data
    global a
    if '+' in new:
        a = int(new.split('+')[1])
        result = int(new.split('+')[0]) + a
        new = str(result)
        data.set(new)
    elif '-' in new:
        a = int(new.split('-')[1])
        result = int(new.split('-')[0]) - a
        new = str(result)
        data.set(new)
    elif '*' in new:
        a = int(new.split('*')[1])
        result = int(new.split('*')[0]) * a
        new = str(result)
        data.set(new)
    elif '/' in new:
        if int(new.split('/')[1]) != 0:
            a = int(new.split('/')[1])
            result = int(int(new.split('/')[0]) / a)
            new = str(result)
            data.set(new)
        else:
            new = 'Cant divide by 0...!'
            data.set(new)
    else:
        pass    
    
    
root.title('Python Calculator')
root.geometry('400x500')
l1  = Label(root, text = '123', font = ('verdana',22),anchor = 'se', textvariable = data)

row1  = Frame(root, background = 'black')
btn1 = Button(row1 , text = '1',command = one_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn2 = Button(row1 , text = '2',command = two_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn3 = Button(row1 , text = '3',command = three_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn10 = Button(row1 , text = '+',command = plus_clicked).pack( expand = True ,fill = 'both', side = 'left')

row2  = Frame(root, background = 'yellow')
btn4 = Button(row2 , text = '4',command = four_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn5 = Button(row2 , text = '5',command = five_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn6 = Button(row2 , text = '6',command = six_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn11 = Button(row2 , text = '-',command = minus_clicked).pack( expand = True ,fill = 'both', side = 'left')

row3  = Frame(root , background = 'red')
btn7 = Button(row3 , text = '7',command = seven_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn8 = Button(row3 , text = '8',command = eight_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn9 = Button(row3 , text = '9', command = nine_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn12 = Button(row3 , text = '*', command = multiple_clicked).pack( expand = True ,fill = 'both', side = 'left')

row4  = Frame(root , background = 'red')
btnC = Button(row4 , text = 'C',command = C_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn0 = Button(row4 , text = '0', command = zero_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn_equal = Button(row4 , text = '=',command = equal_clicked).pack( expand = True ,fill = 'both', side = 'left')

btn13 = Button(row4 , text = '/',command = divide_clicked).pack( expand = True ,fill = 'both', side = 'left')

l1.pack(expand = True, fill = 'both')
row1.pack(expand = True, fill = 'both')
row2.pack(expand = True ,fill = 'both')
row3.pack(expand = True,fill = 'both' )
row4.pack(expand = True,fill = 'both')
mainloop()
