#-*- coding: utf-8 -*-
from Tkinter import *
from interface import UI
from data import DataHandler
from io import FileHandler

def main():
    window = Tk()
    window.title('Student Management Program')
    window.configure(bg="white")
    ui = UI(window)
    datahandler = DataHandler(ui)
    filehandler = FileHandler(datahandler,ui)

    #버튼을 초기화 합니다
    ui.init_btn(datahandler,filehandler)
    window.mainloop()

if __name__ == '__main__':
    main()