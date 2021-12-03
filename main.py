from tkinter import *
from random import *
from myhashmap import myhash


root=Tk()
root.title('Character Scrambler')

mystring=StringVar()
myanswer=Entry(root,font=("Helvetica",24),textvariable=mystring)
myanswer.pack()

my_label = Entry(root,text="",font=("Helvetica",48))
my_label.pack(pady=20)

def myshuffler():
    
    # Break string entered
    myinput=mystring.get()
    break_word = list(myinput)
    
    # Turn shuffled list into word
    fun_word=''
    for letter in break_word:
        fun_word+=getvalue(letter)
        
    my_label.delete(0,END)
    my_label.insert(0,fun_word)

def getvalue(myindex):
    initvalue=myhash[myindex]
    turnvaluetolist=list(initvalue)
    chosenone=choice(turnvaluetolist)
    return chosenone

button_shuffle=Button(root,text='Shuffle now', command=myshuffler)
button_shuffle.pack(pady=20)

root.mainloop()