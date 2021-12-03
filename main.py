from tkinter import *
from random import *


root=Tk()
root.title('Character Scrambler')

my_label = Label(root,text="",font=("Helvetica",48))
# my_label.grid(row=0,column=0)
my_label.pack(pady=20)

def shuffler():
    
    # List of States
    states=['Washington', 'Indiana','California','New York','Texas']
    
    # Pick random word from list
    random_word = choice(states)
    
    # Break word
    break_word = list(random_word)
    shuffle(break_word)
    
    # Turn shuffled list into word
    shuffled_word=''
    for letter in break_word:
        shuffled_word+=letter
        
    my_label.config(text=random_word)
    
shuffler()

root.mainloop()