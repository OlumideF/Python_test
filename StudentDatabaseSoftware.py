#============Frontend==============

from tkinter import *
import tkinter.messagebox
#Import stdDatabase


class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg='cadet blue')

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #==============Frame=============
        MainFrame = Frame(self.root,bg='cadet blue')
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg='Ghost white', relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial',47,'bold'), text='Student Database Management Systems', bg='Ghost white')
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg='Ghost white', relief=RIDGE)
        ButtonFrame.pack(side=TOP)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg='cadet blue', relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = Frame(DataFrame, bd=1, width=1000, height=600, padx=20, pady=20, bg='Ghost white', relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = Frame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg='Ghost white', relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()