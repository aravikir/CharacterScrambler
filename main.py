from tkinter import *
from random import *
import myhashmap


root=Tk()
root.title('Character Scrambler')

mystring=StringVar()
myanswer=Entry(root,font=("Helvetica",24),textvariable=mystring)
myanswer.pack()

my_label = Label(root,text="",font=("Helvetica",48))
my_label.pack(pady=20)

def myshuffler():
    
    # List of States
    states=['Washington', 'Indiana','California','New York','Texas']
    
    # Pick random word from list
    random_word = choice(states)
    
    # Break string entered
    myinput=mystring.get()
    break_word = list(myinput)
    # shuffle(break_word)
    
    # Turn shuffled list into word
    fun_word=''
    for letter in break_word:
        fun_word+=getvalue(letter)
        
    my_label.config(text=fun_word)
    myanswer.delete(0,END)

def getvalue(myindex):
    initvalue=myhashmap[myindex]
    turnvaluetolist=list(initvalue)
    chosenone=choice(turnvaluetolist)
    return chosenone

button_shuffle=Button(root,text='Shuffle now', command=myshuffler)
button_shuffle.pack(pady=20)

root.mainloop()