from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter import messagebox
from shutil import copyfile
import os


master = Tk()
count=0

def addrec():

    f = open('open.txt', 'a')
    vehicle = s1.get()
    type = s2.get()
    company=s3.get()
    engine=s4.get()
    mileage=s5.get()
    f.writelines(vehicle.ljust(10) + type.ljust(10) + company.ljust(10)+engine.ljust(10)+mileage.ljust(10)+"\n")
    f.close()
    deletetext()

def deletetext():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0,END)

def nextrec():
    global count
    f=open('open.txt','r')
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
    list1=l.split()
    if list1.__len__() != 0:
        s1.set(list1[0])
        s2.set(list1[1])
        s3.set(list1[2])
        s4.set(list1[3])
        s5.set(list1[4])
        count = count + 1
    else:
        messagebox.showinfo("ERROR", "END OF THE FILE")
    f.close()
    l6.config(text=count)

def prevrec():
    global count
    if count!=1:
        f=open('open.txt','r')
        i=0
        count = count - 1
        while(i<count):
            l=f.readline()
            i=i+1
        list1=l.split()
        s1.set(list1[0])
        s2.set(list1[1])
        s3.set(list1[2])
        s4.set(list1[3])
        s5.set(list1[4])
        f.close()
        l6.config(text=count)
    else:
        messagebox.showinfo("ERROR","ALREADY AT FIRST ELEMENT OF THE FILE")


def deleterec():
    global count
    infile = open('open.txt', 'r').readlines()
    with open('output.txt', 'w') as outfile:
        for index, line in enumerate(infile):
            if index != count-1:
                outfile.write(line)
    copyfile("output.txt","open.txt")
    os.remove("output.txt")
    deletetext()

def searchdata():
    c=0
    a=0
    vehicle = s1.get()
    f= open("open.txt", "r")
    searchlines = f.readlines()
    for line in searchlines:
        c=c+1
        list1 =line.split()
        if list1[0]==vehicle:
            a=c
            s1.set(list1[0])
            s2.set(list1[1])
            s3.set(list1[2])
            s4.set(list1[3])
            s5.set(list1[4])
            break
    l6.config(text=a)
    f.close()



def updatedata():
    c=l6.cget("text")
    c1=0
    vehicle = s1.get()
    type = s2.get()
    company=s3.get()
    engine=s4.get()
    mileage=s5.get()


    infile = open('open.txt', 'r').readlines()
    with open('output.txt', 'w') as outfile:
        for index, line in enumerate(infile):
            if index != c-1:
                outfile.write(line)
            else:
                outfile.write(vehicle.ljust(10) + type.ljust(10) + company.ljust(10) + engine.ljust(10) + mileage.ljust(10) + "\n")
                messagebox.showinfo("UPDATE", "FILE UPDATED")
    copyfile("output.txt", "open.txt")
    os.remove("output.txt")
    deletetext()

def show_entry_fields():
    print("VEHICLE Name: %s\nTYPE OF VEHICLE: %s" % (s1.get(), s2.get()))

s1 = StringVar()
s2 = StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()

MyFont = font.Font(weight='bold')

label1 = ttk.Label(master, text="VEHICLE NAME",font=MyFont)
label1.grid(row=0,column=2,pady=4)

l2 = Label(master, text="TYPE",font=MyFont)
l2.grid(row=1,column=2,pady=4)

l3 = Label(master, text="COMPANY NAME",font=MyFont)
l3.grid(row=2,column=2,pady=4)

l4 = Label(master, text="ENGINE SIZE",font=MyFont)
l4.grid(row=3,column=2,pady=4)

l5 = Label(master, text="MILEAGE",font=MyFont,height=2, width=20)
l5.grid(row=4,column=2,pady=4)

l6 = Label(master, text="LINE NO.",bg="red",fg="purple", height=2, width=10,font=MyFont)
l6.grid(row=2,column=6,pady=4)

e1 = Entry(master,textvariable=s1,font=MyFont)
e1.grid(row=0, column=3,pady=4)

e2 = Entry(master,textvariable=s2,font=MyFont)
e2.grid(row=1, column=3,pady=4)

e3 = Entry(master,textvariable=s3,font=MyFont)
e3.grid(row=2, column=3,pady=4)

e4 = Entry(master,textvariable=s4,font=MyFont)
e4.grid(row=3, column=3,pady=4)

e5 = Entry(master,textvariable=s5,font=MyFont)
e5.grid(row=4, column=3,pady=4)

Button(master, text='Quit', command=master.quit,bg="gray",font=MyFont,height=2, width=20).grid(row=7, column=2, sticky=W, pady=4)
Button(master, text='SHOW', command=show_entry_fields,bg="gray",font=MyFont,height=2, width=20).grid(row=7, column=3, sticky=W, pady=4)
Button(master, text='ADD', command=addrec,bg="gray",font=MyFont,height=2, width=20).grid(row=7, column=4, sticky=W, pady=4)
Button(master, text='DELETE', command=deleterec,bg="gray",font=MyFont,height=2, width=20).grid(row=8, column=2,sticky=W, pady=4)
Button(master, text="SEARCH",command=searchdata,bg="gray",font=MyFont,height=2, width=20).grid(row=8, column=3, sticky=W, pady=4)
Button(master, text="UPDATE",command=updatedata,bg="gray",font=MyFont,height=2, width=20).grid(row=8, column=4, sticky=W, pady=4)

Button(master, text='>', command=nextrec,height=2, width=20,bg="gray",font=MyFont).grid(row=5, column=4, sticky=W, pady=4)
Button(master, text='<', command=prevrec,height=2, width=20,bg="gray",font=MyFont).grid(row=5, column=2, sticky=W, pady=4)

master.mainloop()
