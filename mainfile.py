from tkinter import *
import sqlite3
import back
import mailing
from tkinter import messagebox
from tkinter import font  

def mail_validator(email):
    if '@gmail.com' == email[len(email)-10:]:
        return 1
    else:
        return 0

def loginpage():
    root = Tk()
    header = font.Font(family='ComicSansMS', size=15, weight='bold', underline=0)
    lable_font = font.Font(family='Arial',size=12, weight='bold')
    entry_font = font.Font(family='Arial',size=12)
    simple = font.Font(family='Arial',size=11)

    def forgpass():
        forg = Tk()

        def message():
            x = back.checking(e1.get())
            messagebox.showinfo('Alert','If provided email is valid we will send back a mail with password and some times mail can be even in spam block so verify it.')
            if x is not None:
                mailing.connection(e1.get(),x)
            forg.destroy()

        l1 = Label(forg, text='Email Id', font=lable_font, bg='azure')
        l1.place(x=30,y=60)
        e1 = Entry(forg, font=entry_font, bg='light cyan', fg='purple')
        e1.place(x=100, y=60)
        b1 = Button(forg, text="Submit", font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=message)
        b1.place(x=80, y=100)
        forg.title('Forgot Password')
        forg.configure(background='azure')
        forg.geometry('300x350+50+50')
        forg.mainloop()

    def registerpage():
        root.destroy()
        reg = Tk()

        def add_user(email,password):
            if mail_validator(email):
                if password == '':
                    messagebox.showerror('Alert','Password cannot be empty.')
                else:
                    if back.inserting_user(email,password):
                        messagebox.showinfo('Sucess','Account created sucessfully.')
                        reg.destroy()
                        loginpage()
                    else:
                        messagebox.showerror('Failure','Account already exists.')
            else:
                messagebox.showerror('Alert','Email seems to be wrong.')
                 

        l1 = Label(reg, text='Email', font=lable_font, bg='azure')
        l1.place(x=40, y=60)
        e1 = Entry(reg, font=entry_font, bg='light cyan', fg='purple')
        e1.place(x=100, y=60)

        l2 = Label(reg, text='Password', font=lable_font, bg='azure')
        l2.place(x=20, y=100)
        e2 = Entry(reg, font=entry_font, bg='light cyan', fg='purple')
        e2.place(x=100, y=100)

        b1 = Button(reg, text='Sign Up', font=entry_font, bg='mint cream', fg='purple', height=1, width=12,command=lambda :add_user(e1.get(),e2.get()))
        b1.place(x=80, y=140)

        l3 = Label(reg, text='Please make sure you provide correct email', font=entry_font, fg='red', bg='azure')
        l3.place(x=20,y=180)

        reg.configure(background='azure')
        reg.title('Registration Page')
        reg.geometry('350x300+50+50')
        reg.mainloop()

    def password_updater():
        root.destroy()
        new_root = Tk()

        def check():
            if e1.get() != '' and e2.get() != '' and e3.get() != '':
                if back.validate_user(e1.get(),e2.get()):
                    back.update_user(e1.get(),e3.get())
                    new_root.destroy()
                    loginpage()
                else:
                    messagebox.showerror("Error","No such users available.")
            else:
                messagebox.showerror("Error","Empty values cannot be considered.")

        l1 = Label(new_root, text='Email Id', font=lable_font, bg='azure')
        l1.place(x=50, y=60)
        e1 = Entry(new_root, font=entry_font, bg='light cyan', fg='purple')
        e1.place(x=120, y=60)    
        
        l2 = Label(new_root, text='Old Password', font=lable_font, bg='azure')
        l2.place(x=10, y=100)
        e2 = Entry(new_root, font=entry_font, bg='light cyan', fg='purple')
        e2.place(x=120, y=100)
        
        l3 = Label(new_root, text='New Password', font=lable_font, bg='azure')
        l3.place(x=10, y=140)
        e3 = Entry(new_root, font=entry_font, bg='light cyan', fg='purple')
        e3.place(x=120, y=140)

        b1 = Button(new_root, text='Submit', font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=check)
        b1.place(x=120, y=180)

        new_root.title('Password Updater')
        new_root.configure(background='azure')
        new_root.geometry('330x250+50+50')
        new_root.mainloop()


    def validator(mail,password):
        x = back.validate_user(mail,password)
        if x == 0:    
            e1.delete(0,END)
            e2.delete(0,END)
            messagebox.showerror('Login Failed','Email and password did not match')
            
        else:
            mainpage(x[1])

    
    def mainpage(id):
        num = id
        root.destroy()
        main_page = Tk()

        def checker():
            if e1.get() != '' and e2.get() != '' and e3.get() != '':
                return 1
            else:
                return 0

        def viewall():
            list1.delete(0,END)
            for i in back.view(num):
                list1.insert(END,i)
        
        def add_pass():
            if checker():
                if back.duplicate(num,e1.get(),e2.get(),e3.get()):
                    back.inserting_pass(num,e1.get(),e2.get(),e3.get())
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                else:
                    messagebox.showerror("Error","Duplicate values cannot be added.")        
            else:
                messagebox.showerror("Error","Empty values cannot be added.")
            viewall()

        def del_pass():
            if checker():
                if back.duplicate(num,e1.get(),e2.get(),e3.get()):
                    messagebox.showerror("Error","No such record is found in your data.")
                else:
                    back.del_pass(num,e1.get(),e2.get(),e3.get())
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    viewall()
            else:
                messagebox.showerror("Error","All the values in entry are required")

        def del_all():
            back.del_pass_all(num)
            viewall()

        def get_selected_row(event):
            global selected_tuple
            index = list1.curselection()[0]
            selected_tuple = list1.get(index)
            # print(selected_tuple)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[0])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[1])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[2])

        l1 = Label(main_page, text='Website:', font=lable_font, bg='azure')
        l1.place(x=80, y=60)
        e1 = Entry(main_page, font=entry_font, bg='light cyan', fg='purple')
        e1.place(x=170, y=60)    
        
        l2 = Label(main_page, text='Email Id:', font=lable_font, bg='azure')
        l2.place(x=80, y=100)
        e2 = Entry(main_page, font=entry_font, bg='light cyan', fg='purple')
        e2.place(x=170, y=100)
        
        l3 = Label(main_page, text='Password:', font=lable_font, bg='azure')
        l3.place(x=80, y=140)
        e3 = Entry(main_page, font=entry_font, bg='light cyan', fg='purple')
        e3.place(x=170, y=140)

        list1 = Listbox(main_page, height=10, width=35)
        list1.place(x=40, y=200)
        sb1 = Scrollbar(main_page)
        sb1.place(x=260, y=200)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        list1.bind("<<ListboxSelect>>",get_selected_row)
        
        b1 = Button(main_page, text='View All',font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=viewall)
        b1.place(x=290, y=180)
        b2 = Button(main_page, text='Add Password',font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=add_pass)
        b2.place(x=290, y=220)
        b3 = Button(main_page, text='Delete',font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=del_pass)
        b3.place(x=290, y=260)
        b4 = Button(main_page, text='Delete All',font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=del_all)
        b4.place(x=290, y=300)
        b5 = Button(main_page, text='Quit',font=entry_font, bg='mint cream', fg='purple', height=1, width=12, command=main_page.destroy)
        b5.place(x=290, y=340)

        main_page.configure(background='azure')
        main_page.title('Main Page')
        main_page.geometry('500x500+50+50')
        main_page.mainloop()

    heading = Label(root, text='Login Page', font=header, fg='blue', bg='azure')
    heading.place(x=180,y=10)

    l1 = Label(root, text='Email Id:', font=lable_font, bg='azure')
    l1.place(x=110, y=60)
    e1 = Entry(root, font=entry_font, bg='light cyan', fg='purple')
    e1.place(x=200, y=60)

    l2 = Label(root, text='Password:', font=lable_font, bg='azure')
    l2.place(x=110, y=100)
    e2 = Entry(root, font=entry_font, bg='light cyan', fg='purple')
    e2.place(x=200, y=100)

    b1 = Button(root, text='Login', font=entry_font, bg='mint cream', fg='purple', height=1, width=8, command=lambda: validator(e1.get(),e2.get()))
    b1.place(x=190, y=140)

    l3 = Label(root, text='Dont have account? Click the button', font=simple, bg='azure', fg='firebrick1')
    l3.place(x=30, y=200)
    b2 = Button(root, text='Sign Up', font=entry_font, bg='mint cream', fg='purple', height=1, width=8, command=registerpage)
    b2.place(x=280, y=195)

    l4 = Label(root, text='Forgot Password? Click the button', font=simple, bg='azure', fg='firebrick1')
    l4.place(x=30, y=240)
    b3 = Button(root, text='Forget Password', font=entry_font, bg='mint cream', fg='purple', height=1, width=15,command=forgpass)
    b3.place(x=270, y=235)

    l5 = Label(root, text='Update Password', font=simple, bg='azure',fg='firebrick1')
    l5.place(x=50, y=285)
    b4 = Button(root, text='Update Password', font=entry_font, bg='mint cream', fg='purple', height=1, width=15, command=password_updater)
    b4.place(x=180, y=280)

    l6 = Label(root, text='Note : ',font=simple, bg='azure', fg='black')
    l6.place(x=40, y=320)
    l7 = Label(root, text='We never share your email and passwords with anyone', font=simple, bg='azure', fg='black')
    l7.place(x=40, y=340)

    root.title('Login Page')
    root.geometry("500x400+50+50")
    root.configure(background='azure')
    root.mainloop()

loginpage()