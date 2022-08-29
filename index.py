from cProfile import label
from cgitb import text
from curses import window
from email.mime import application
import this
from tkinter import ttk
from tkinter import *

import sqlite3
from tkinter.tix import COLUMN
from turtle import title

class product:
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('product application')
        
        #creating a frame container
        frame = LabelFrame(self.wind, text= 'register a new product')
        frame.grid(row=0,column=0,columnspan=3,pady=20)
        
        #name input
        label(frame, text='Name:').grid(row = 1, colum = 0 )
        self.name = Entry(frame)
        self.name.focus()
        self. name. grid(row = 1, column=1)
        
        #Price Input
        label(frame, text='price:').grid(Row=2,column=0)
        self.name = Entry(frame)
        self.name.grid(row = 2, column= 1)
        
        # Buttom Add Product
        ttk.Button(frame, text="save product").grid(row = 3, columnspan=2, sticky= W + E) 
        
        #table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row = 4,column= 0, columnspan= 2)
        self.tree.heading('#0', text='name', anchor=CENTER)
        self.tree.heading('#1', text='price',anchor= CENTER)
         
if __name__== '__main__':
        window = Tk()
        application = product(window)
        window.mainloop()
        