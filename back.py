import sqlite3
from tkinter import messagebox

def connection():
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists MainTable(
        id integer primary key,
        email text unique,
        password text
    )'''
    )
    cur.execute('''
    create table if not exists SubTable(
        id integer,
        website text,
        email text,
        password text,
        foreign key(id) references MainTable(id)
    )'''
    )
    conn.commit()
    conn.close()

def inserting_user(email,password):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        cur.execute("insert into MainTable values(NULL,?,?)",(email,password))
    except:
        return 0
    conn.commit()
    conn.close()
    return 1

def validate_user(email,password):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("select password,id from MainTable where email=?",(email,))
    passkey = cur.fetchone()
    if passkey is None:
        return 0
    else:
        if(passkey[0] == password):
            return 1,passkey[1]
        else:
            return 0
    conn.commit()
    conn.close() 

def checking(email):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute('select password from MainTable where email=?',(email,))
    x = cur.fetchone()
    conn.commit()
    conn.close()
    if x == None:
        return 0
    else:
        return x[0]
    

def update_user(email,password):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute('update MainTable set password=? where email=?',(password,email))
    messagebox.showinfo('Success','Password updated sucessfully.')
    conn.commit()
    conn.close()

def inserting_pass(number,website,email,password):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        cur.execute("insert into SubTable values(?,?,?,?)",(number,website,email,password))
    except:
        return 0
    conn.commit()
    conn.close()
    return 1

def del_pass(num,website,email,password):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("delete from SubTable where id=? and website=? and email=? and password=?",(num,website,email,password))
    conn.commit()
    conn.close()

def del_pass_all(num):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("delete from SubTable where id=?",(num,))
    conn.commit()
    conn.close()


def view(id):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("select website,email,password from SubTable where id=?",(id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def duplicate(id,website,email,password):
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        cur.execute("select id from SubTable where id=? and website=? and email=? and password=?",(id,website,email,password))
        x = cur.fetchone()
    except:
        return 0
    if x is None:
        return 1
    conn.commit()
    conn.close()
    return 0

connection()