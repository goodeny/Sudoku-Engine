from tkinter import *

class Buttons:
    def __init__(self, window, row, indice):
        self.window = window
        self.row = row
        self.indice = indice
        self.number = 0
 
    def generate(self,x1 ,y1,img):
        self.load_block_img = PhotoImage(file='assets/block.png')

        self.block = Label(self.window, image=img, width=48,height=48, bg='#373941')
        self.block.place(x=x1,y=y1)

        self.entry = Entry(self.block, width=2, font='Arial 30',justify="center", bg='white', fg='black', bd=0)
        self.entry.place(x=0, y=0)
        