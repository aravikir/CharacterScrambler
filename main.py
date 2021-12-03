from tkinter import *
from random import *


root=Tk()
root.title('Character Scrambler')
root.iconbitmap('D:\Abhishek Ravikiran\OneDrive\My Documents\MyGit\CharacterScrambler\CharacterScrambler.ico')
root.geometry("600x400+-1900+100")

my_label = Label(root,text="",font=("Helvetica",48))
my_label.pack()

def shuffle():
    
    # List of States
    states=['Washington', 'Indiana','California','New York','Texas']
    
    # Pick random word from list
    random_word = choice(states)
    my_label.config(text=random_word)
    
shuffle()

root.mainloop()