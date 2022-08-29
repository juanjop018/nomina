from cProfile import label
from cgitb import text
from curses import window
from email.mime import application
from hashlib import new
from inspect import Parameter
from optparse import Values
from sqlite3.dbapi2 import _Parameters
from sre_constants import SUCCESS
import string
import this
from tkinter import ttk
from tkinter import *

import sqlite3
from tkinter.tix import COLUMN
from turtle import title
from typing_extensions import Self
from unicodedata import name
from unittest import result

class product:
    db_name ='database.db'
    
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
        ttk.Button(frame, text="save product", command = self.add_product).grid(row = 3, columnspan=2, sticky= W + E) 
        
        #Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row = 3,column= 0, columnspan = 2, sticky = W + E )
        
        #table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row = 4,column= 0, columnspan= 2)
        self.tree.heading('#0', text='name', anchor=CENTER)
        self.tree.heading('#1', text='price',anchor= CENTER)
        
        #buttons
        ttk.Button(text = 'DELETE', command = self.delete.product).igrid(row = 5, column = 0, sticky = W +E)
        ttk.Button(text = 'EDIT', command = self.edit_product).igrid(row = 5, column = 1, sticky = W +E)
        
        #Filling the row
        self.get_producs()
         
    def run_query(self,query,parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
         Cursor = conn.cursor()
         result = Cursor.execute(query, parameters)
         conn.commit()
         return result
     
    def get_producs(self):
        # cleaning table
        records = self.tree.get_childres()
        for element in records:
            self.tree.delete(element)
        # quering data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('',0,text = row[1],values = row[2])
            
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get())
    
    def add_product (self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            Parameters = (self.name.get(), self.price.get())
            self.run_query(query, Parameters)
            self.message['text']= 'product {} added Successfully'.format(self.name.get())
            self.name.delete(0,END)
            self.price.delete(0,END)
        else:
            print.message['text']='Name and Price are Required'
        self.get_producs()
        
        def delete_product(self):
          self.message['text'] = ''
          try:
            self.tree.item(self.tree.selection())['text'][0]
          except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return
          self.message['text'] = ''
          name = self.tree.item(self.tree.selection())['text']
          query = 'DELETE FROM product WHERE name = ?'
          self.run_query(query, (name,))
          self.message['text'] = 'Record {} deleted Successfully'.format(name)
          self.get_products()
            
        def edit_product(self):
            self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        
        #Old Name
        Label(self.edit_wind, text = 'Old Name: ').grid(row = 2, column = 1)
        Entry(Self.edit_wind, textvariable = StringVar (self.edit_wind, Value = name),state = 'reandonly').grid(row = 0, column = 2)
        
        #New Name
        label(self.edit_wind, text = 'New Name').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)
        
        #Old Price
        Label(self.edit_wind, text = 'Old Price').grid(row = 2, colum = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        
        #New Price
        Label(self.edit_wind, text = 'New price').grid(row = 3, column = 1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)
        
        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2,sticky = W)
        def edit_records(self,new_name,name,new_price,old_price):
            query = 'UPDATE product SET name = ?, price = ?, WHERE name = ? AND price = ?'
            Parameter = (new_name, new_price, name, old_price)
            self.run_query(query.parameters)
            self.edit_wind.destroy()
            self.message['text'] = 'record {} updated Successfully'.format(name)
            self.get_product()
        
if __name__== '__main__':
        window = Tk()
        application = product(window)
        window.mainloop()
        