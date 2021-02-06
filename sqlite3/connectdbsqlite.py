from os import close
import sqlite3

"""
Documentacao

"""

class Conectadb:
    
    def __init__(self):
        self.conn = sqlite3.connect('clientes.db')


'''
conn = sqlite3.connect('clientes.db')
curr = conn.cursor()
'''

def create_table():
    curr.execute('''CREATE TABLE registro ('\
        'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
        'nome TEXT,'\
        'status TEXT))'''





def data_insert():


def data_read():


def data_update():


def data_delete():



curr.close()

conn.close()



