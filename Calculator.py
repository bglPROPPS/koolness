#demonstrates how to use a class with Tkinter

from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """


    def __init__(self, master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        
        self.grid()
        
        self.create_widgets()

    
    def create_widgets(self):
        
        

        self.answer = Entry(self)
        self.answer.grid(row = 0,column = 4, sticky = NW)

        self.buttonEquals = Button(self,text="=", command = self.solve)
        self.buttonEquals.grid(row = 7, column = 2, sticky = W)

        self.button1 = Button(self,text="1",command = lambda: self.answer.insert(END,"1"))
        self.button1.grid(row=6,column = 0, sticky = W)

        self.button2 = Button(self,text="2",command = lambda: self.answer.insert(END,"2"))
        self.button2.grid(row=6,column = 1, sticky = W)

        self.button3 = Button(self,text="3",command = lambda: self.answer.insert(END,"3"))
        self.button3.grid(row=6,column = 2, sticky = W)

        self.button4 = Button(self,text="4",command = lambda: self.answer.insert(END,"4"))
        self.button4.grid(row=5,column = 0, sticky = W)

        self.button5 = Button(self,text="5",command = lambda: self.answer.insert(END,"5"))
        self.button5.grid(row=5,column = 1, sticky = W)

        self.button6 = Button(self,text="6",command = lambda: self.answer.insert(END,"6"))
        self.button6.grid(row=5,column = 2, sticky = W)

        self.button7 = Button(self,text="7",command = lambda: self.answer.insert(END,"7"))
        self.button7.grid(row=4,column = 0, sticky = W)

        self.button8 = Button(self,text="8",command = lambda: self.answer.insert(END,"8"))
        self.button8.grid(row=4,column = 1, sticky = W)

        self.button9 = Button(self,text="9",command = lambda: self.answer.insert(END,"9"))
        self.button9.grid(row=4,column = 2, sticky = W)

        self.button0 = Button(self,text="0",command = lambda: self.answer.insert(END,"0"))
        self.button0.grid(row=7,column = 0, sticky = W)

        self.buttonPlus = Button(self,text="+",command = lambda: self.answer.insert(END,"+"))
        self.buttonPlus.grid(row=7,column = 3, sticky = W)

        self.buttonMinus = Button(self,text="-",command = lambda: self.answer.insert(END,"-"))
        self.buttonMinus.grid(row=6,column = 3, sticky = W)

        self.buttonMul = Button(self,text="x",command = lambda: self.answer.insert(END,"*"))
        self.buttonMul.grid(row=5,column = 3, sticky = W)

        
        self.buttonDiv = Button(self,text="/",command = lambda: self.answer.insert(END,"/"))
        self.buttonDiv.grid(row=4,column = 3, sticky = W)

        self.buttonDot = Button(self,text=".",command = lambda: self.answer.insert(END,"."))
        self.buttonDot.grid(row=7,column = 1, sticky = W)

        self.buttonRight = Button(self,text=")",command = lambda: self.answer.insert(END,")"))
        self.buttonRight.grid(row=0,column = 1, sticky = W)

        self.buttonLeft = Button(self,text="(",command = lambda: self.answer.insert(END,"("))
        self.buttonLeft.grid(row=0,column = 0, sticky = W)

        self.buttonClear = Button(self,text="C",command = lambda: self.answer.delete("0",END))
        self.buttonClear.grid(row=0,column = 2, sticky = W)
      

    def solve(self):
        
        
        content = self.answer.get()
        self.answer.delete("0",END)
        content = content.replace('^', "**")
       
        message = eval(content)

        
        self.answer.insert("0",message)
    
root = Tk()
root.title("Password")
root.geometry("300x150")
app = Application(root)

root.mainloop()
        
