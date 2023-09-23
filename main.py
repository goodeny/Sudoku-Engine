import os
os.system('pip install py-sudoko')
os.system('pip install keyboard')
from tkinter import *
from sudoku_buttons import Buttons
from sudoku_matriz import board
from sudoku import Sudoku
import keyboard
import time
import threading
import os

class App:
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='#373941')
        self.window.geometry('960x698')
        self.window.title('Sudoku Engine')
        self.window.resizable(0,0)
        self.entries = []
        self.numbers = []
        self.solution = []
        self.value_slider = DoubleVar()
        self.install_lib()
        self.create_logo()
        self.create_slider()
        self.generate_buttons()
        self.create_button_restart()
        self.windows_blocks()
        self.create_button_solve()
    
    def windows_blocks(self):
        self.w_blocks = Frame(self.window, height=550, width=600, bg='#373941')
        self.w_blocks.place(x=0, y=100)
        self.generate_matriz_block()

    def generate_matriz_block(self):
        self.entries[0:8].clear()
        self.pady = 10
        self.padx = 30
        self.row = 0
        self.indice = 0
        self.count = 0
        self.load_block_img = PhotoImage(file='assets/block.png')
        for i in range(9*9):      
            self.button_generate = Buttons(self.w_blocks, self.row, self.indice)
            self.button_generate.generate(self.padx+(self.count*57),self.pady, self.load_block_img)
            self.entries.append(self.button_generate.entry)
            self.indice += 1
            self.count += 1
            if self.count == 9:
                self.row += 1
                self.indice = 0
            if self.count == 9:
                self.count = 0
                self.pady += 60
                self.padx = 30
            #print(f'Row: {self.button_generate.row} Indice: {self.button_generate.indice}')
                    
    def create_logo(self):
        self.logo_bg = PhotoImage(file='assets/logo.png', )
        self.logo_label = Label(self.window, image=self.logo_bg, bg='#373941')
        self.logo_label.place(x=30,y=30)

    def create_slider(self):
        self.label_slider = Label(self.window, text='On bad computers lower values ​​may give wrong results \n\n| Hyper Boost: 0 | Medium: 1 | Recommended: 2 |', fg='white', bg='#373941')
        self.label_slider.place(x=617, y=400)

        self.slider = Scale(self.window, from_=0, to=100, resolution=1.0 ,orient='horizontal', variable=self.value_slider, command=self.update, bg='#373941', bd=0, activebackground="#373941", fg='white', highlightbackground='#373941', length=260)  
        self.slider.place(x=630, y=450)
        
    def create_button_solve(self):
        self.button_solve_img = PhotoImage(file='assets/button_solve.png')
        self.button_solve = Button(self.window, image=self.button_solve_img, bg='#373941', activebackground='#373941', bd=0, cursor='hand2', command=lambda: threading.Thread(target=self.generate_sudoku).start())
        self.button_solve.place(x=630, y=500)

    def create_button_solving(self):
        self.button_solving_img = PhotoImage(file='assets/button_solving.png')
        self.button_solving = Button(self.window, image=self.button_solving_img, bg='#373941', cursor='hand2', activebackground='#373941', bd=0)
        self.button_solving.place(x=630, y=500)

    def create_button_restart(self):
        self.button_restart_img = PhotoImage(file='assets/button_restart.png')
        self.button_restart = Button(self.window, image=self.button_restart_img, bd=0, bg='#373941', cursor='hand2', command=lambda: threading.Thread(target=self.restart).start())
        self.button_restart.place(x=630, y=580)

    def generate_sudoku(self):
        self.button_solve.destroy()
        self.create_button_solving()
        board.clear()   
        self.numbers.clear()
        for i, entry in enumerate(self.entries):
            valor = entry.get()
            if valor != "":
                self.numbers.append(int(valor))
            else:
                self.numbers.append(0)
        matriz = [self.numbers[i:i+9] for i in range(0, len(self.numbers), 9)]
        for i in matriz:
            board.append(i)

        #print(self.entries)
        #print(board)
        if board == [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]:
            self.button_solving.destroy()
            self.create_button_solve()
        else:
            self.solve_sudoku()
    
    def generate_buttons(self):
        x1=620
        y1=100

        imgs = ['assets/buttons/1.png',
                'assets/buttons/2.png',
                'assets/buttons/3.png',
                'assets/buttons/4.png',
                'assets/buttons/5.png',
                'assets/buttons/6.png',
                'assets/buttons/7.png',
                'assets/buttons/8.png',
                'assets/buttons/9.png',
                ]
        
        self.button_pad_img1 = PhotoImage(file=imgs[0])
        self.button_pad_img2 = PhotoImage(file=imgs[1])
        self.button_pad_img3 = PhotoImage(file=imgs[2])
        self.button_pad_img4 = PhotoImage(file=imgs[3])
        self.button_pad_img5 = PhotoImage(file=imgs[4])
        self.button_pad_img6 = PhotoImage(file=imgs[5])
        self.button_pad_img7 = PhotoImage(file=imgs[6])
        self.button_pad_img8 = PhotoImage(file=imgs[7])
        self.button_pad_img9 = PhotoImage(file=imgs[8])

        self.button_pad = Button(self.window,image=self.button_pad_img1, text=1, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(1))
        self.button_pad.place(x=x1,y=y1)

        self.button_pad = Button(self.window,image=self.button_pad_img2, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(2))
        self.button_pad.place(x=x1+100,y=y1)

        self.button_pad = Button(self.window,image=self.button_pad_img3, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(3))
        self.button_pad.place(x=x1+200,y=y1)

        self.button_pad = Button(self.window,image=self.button_pad_img4, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(4))
        self.button_pad.place(x=x1,y=y1+100)

        self.button_pad = Button(self.window,image=self.button_pad_img5, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(5))
        self.button_pad.place(x=x1+100,y=y1+100)

        self.button_pad = Button(self.window,image=self.button_pad_img6, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(6))
        self.button_pad.place(x=x1+200,y=y1+100)

        self.button_pad = Button(self.window,image=self.button_pad_img7, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(7))
        self.button_pad.place(x=x1,y=y1+200)

        self.button_pad = Button(self.window,image=self.button_pad_img8, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(8))
        self.button_pad.place(x=x1+100,y=y1+200)

        self.button_pad = Button(self.window,image=self.button_pad_img9, bd= 0, bg="#373941", activebackground="#373941", cursor='hand2',command=lambda: self.input_number(9))
        self.button_pad.place(x=x1+200,y=y1+200)

    def input_number(self, n):
        keyboard.press(f'{n}')

    def update(self, event=None):
        current_value = self.value_slider.get() / 10.0
        #print(f'value: {current_value}')

    def solve_sudoku(self):
        puzzle = Sudoku(3, 3, board=board)
        solution = puzzle.solve()
        #print(solution.board)
        for i in solution.board:
            for y in i:
                self.solution.append(y)
        #print(self.solution)
        self.fill_website()

    def fill_software(self):
        for i, entry in enumerate(self.entries):
                entry.delete(0,END)
                entry.insert(0, self.solution[i])
        time.sleep(2)

    def restart(self):
        self.solution.clear()
        self.numbers.clear()
        for i, entry in enumerate(self.entries):
                entry.delete(0,END)
        
    def fill_website(self):
        time.sleep(5)
        count = 1
        for i in range(0,81):
            if keyboard.is_pressed('0'):
                break
            else:
                try:
                    time.sleep(self.value_slider.get() / 10.0)
                    keyboard.press(f'{self.solution[i]}')
                    keyboard.press('right')
                    if count == 9:
                        keyboard.press('down')
                        for i in range(9):
                            keyboard.press('left')
                        count = 0
                    count += 1
                except:
                    self.button_solving.destroy()
                    self.create_button_solve()
        self.fill_software()
        self.button_solving.destroy()
        self.create_button_solve()

    def install_lib(self):
        try:
            print('Installing dependencies...\nDev by: Goodeny\nhttps://github.com/goodeny')
            os.system('pip install py-sudoku')
            os.system('pip install keyboard')
        except:
            os.system('Try install "pip install py-sudoku"\n"pip install keyboard"\nDirect download: https://github.com/goodeny/Sudoku-Engine')

if __name__ == "__main__":
    app = App()
    app.window.mainloop()
