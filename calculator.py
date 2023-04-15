from tkinter import *
from tkinter import ttk
from romans import RomanNumber


normal_buttons = [
    {
        "text": "1",
        "col": 0,
        "row": 4,
    },
    {
        "text": "2",
        "col": 1,
        "row": 4,
    },
    {
        "text": "3",
        "col": 2,
        "row": 4,
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
    },
    {
        "text": "4",
        "col": 0,
        "row": 3,
    },
    {
        "text": "5",
        "col": 1,
        "row": 3,
    },
    {
        "text": "6",
        "col": 2,
        "row": 3,
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
    },
    {
        "text": "7",
        "col": 0,
        "row": 2,
    },
    {
        "text": "8",
        "col": 1,
        "row": 2,
    },
    {
        "text": "9",
        "col": 2,
        "row": 2,
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
    },
    {
        "text": "C",
        "col": 1,
        "row": 1,
    },
    {
        "text": "+/-",
        "col": 2,
        "row": 1,
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1,
    },
    {
        "text": "0",
        "col": 0,
        "row": 5, 
        "W": 2,
    },
    {
        "text": ",",
        "col": 2,
        "row": 5,
    },
    {
        "text": "=",
        "col": 3,
        "row": 5,
    }
]

roman_buttons = [
    {
        "text": "=",
        "col": 0,
        "row": 5,
        "W": 4
    },
    {
        "text": "I",
        "col": 0,
        "row": 4,
    },
    {
        "text": "V",
        "col": 1,
        "row": 4,
    },
    {
        "text": "X",
        "col": 0,
        "row": 3,
    },
    {
        "text": "L",
        "col": 1,
        "row": 3,
    },
    {
        "text": "C",
        "col": 0,
        "row": 2,
    },
    {
        "text": "D",
        "col": 1,
        "row": 2,
    },
    {
        "text": "M",
        "col": 2,
        "row": 2,
        "H": 3
    },
    {
        "text": "AC",
        "col": 1,
        "row": 1,
        "W": 2
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1,
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
    }
]

def pinta(valor):
    print(valor)
    return valor

class Controller(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=300)
        self.reset()
        self.status = "N"

        self.display = Display(self)
        self.display.grid(column=0, row=0)

        self.keyboard = Keyboard(self, self.set_operation, self.status)
        self.keyboard.grid(column=0, row=1)

        self.selector = Selector(self.keyboard, self.change_status, self.status)
        self.selector.grid(column=0, row=1)

    def reset(self):
        self.op1 = None
        self.op2 = None
        self.operation = ''
        self.displayValue = '0'
        self.just_pressed_sign = False

    def to_float(self, valor):
        return float(valor.replace(',', '.'))

    def to_str(self, valor):
        return str(valor).replace('.', ',')

    def calculate(self):
        if self.operation == '+':
            return self.op1 + self.op2
        elif self.operation == '-':
            return self.op1 - self.op2
        elif self.operation == 'x':
            return self.op1 * self.op2
        elif self.operation == '÷':
            return self.op1 / self.op2

        return self.op2

    def set_operation(self, something):

        if self.status == "R":
            self.set_operation_R(something)
        else:
            self.set_operation_N(something)
            
        self.display.paint(self.displayValue)

    def set_operation_R(self, something):
        print("Developing")

    def set_operation_N(self, something):
        if something.isdigit(): # Check if something is in (IVXLCDM) and check if the roman numeral is formatted correctly. Change displayValue
            if self.displayValue == "0" or self.just_pressed_sign:
                self.op1 = self.to_float(self.displayValue)
                self.op2 = None
                self.displayValue = something
            else:
                self.displayValue += str(something)
        
        if something == 'C': # and it is Arabic if it is not 'AC'
            self.reset()

        if something == '+/-' and self.displayValue != '0': # Does not work in roman
            if self.displayValue[0] == '-':
                self.displayValue = self.displayValue[1:]
            else:
                self.displayValue = '-' + self.displayValue

        if something == ',' and ',' not in self.displayValue: # Does not work in roman
            self.displayValue += str(something)

        if something == '+' or something == '-' or something =='x' or something =='÷':
            if not self.op1:
                self.op1 = self.to_float(self.displayValue) # Pass to RomanNumber if status is R
                self.operation = something
            elif not self.op2:
                self.op2 = self.to_float(self.displayValue) # Pass to RomanNumber if status is R
                res = self.calculate()
                self.displayValue = self.to_str(res)
                self.operation = something
            else: 
                self.op1 = self.to_float(self.displayValue) # Pass to RomanNumber if status is R
                self.op2 = None
                self.operation = something
            self.just_pressed_sign = True
        else:
            self.just_pressed_sign = False

        if something == '=':
            if self.op1 and not self.op2:
                self.op2 = self.to_float(self.displayValue)
                res = self.calculate()
                self.displayValue = self.to_str(res)

            elif self.op1 and self.op2:
                self.op1 = self.to_float(self.displayValue)
                res = self.calculate()
                self.displayValue = self.to_str(res)



    def change_status(self, status):
        self.status = status
        self.keyboard.status = status
        self.reset()
        

class Display(ttk.Frame):
    value = "0"
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        self.lbl = ttk.Label(self, text=self.value, anchor=E, style='my.TLabel')
        self.lbl.pack(side=TOP, fill=BOTH, expand=True)

    def paint(self, something):
        self.value = something
        self.lbl.config(text=something)

        
class Selector(ttk.Frame):
    def __init__(self, parent, command, status="N"):
        ttk.Frame.__init__(self, parent, width=68, height=50)
        self.status = status
        self.__value = StringVar()
        self.__value.set(self.status)
        self.command = command

        radioB1 = ttk.Radiobutton(self, text="N", value="N", name="rbtn_normal", variable=self.__value, command=self.__click)
        radioB1.place(x=0, y=5)
        radioB2 = ttk.Radiobutton(self, text="R", value="R", name="rbtn_romano", variable=self.__value, command=self.__click)
        radioB2.place(x=0, y=30)

    def __click(self):
        self.status = self.__value.get()
        self.command(self.status)



class Keyboard(ttk.Frame):
    def __init__(self, parent, command, status="N"):
        ttk.Frame.__init__(self, parent, height=250, width=272)
        self.__status = status
        self.buttonListRomans = []
        self.buttonListNormal = []
        self.command = command
        
        if self.__status == "N":
            self.normalPaint()
        else:
            self.romanPaint()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor
        if valor == 'N':
            self.normalPaint()
        else:
            self.normalRoman()

    def normalPaint(self):
        if len(self.buttonListNormal) == 0:
            for properties in normal_buttons:
                btn = CalcButton(self, properties['text'], self.command, properties.get("W", 1), properties.get("H", 1))
                self.buttonListNormal.append((btn, properties))
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))
        else:
            for btn, properties in self.buttonListNormal: 
                 btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))

        for delete, properties in self.buttonListRomans:
            delete.grid_forget()

    def normalRoman(self):
        if len(self.buttonListRomans) == 0:
            for properties in roman_buttons:
                btn = CalcButton(self, properties['text'], self.command, properties.get("W", 1), properties.get("H", 1))
                self.buttonListRomans.append((btn, properties))
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))
        else:
            for btn, properties in self.buttonListRomans:
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))

        for delete, properties in self.buttonListNormal:
            delete.grid_forget()



class CalcButton(ttk.Frame):
    def __init__(self, parent, value, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=68*width, height=50*height)
        self.pack_propagate(0)

        btn = ttk.Button(self, text=value, command=lambda: command(value))
        btn.pack(side=TOP, fill=BOTH, expand=True)