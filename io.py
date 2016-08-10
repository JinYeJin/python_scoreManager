#-*- coding: utf-8 -*-
from Tkinter import *

class FileHandler:
    def __init__(self,dataHandler,UI):
        self.ui = UI
        self.datahandler = dataHandler
    def outFile(self):
        self.ui.clear_status()
        self.fileName =self.ui.entry_list[7].get().strip()
        if self.fileName == "":
            self.ui.text_status.insert(END,"[저장 실패] 파일이름이 공백 입니다.")
            return

        f = open("./"+self.fileName+".txt",'w')
        for k,v in self.datahandler.data_dic.items():
            f.write(str(k)+"\t" + v[0] + "\t" + str(v[1])+"\n")
        f.close()
        self.ui.entry_list[7].delete(0,END)
        self.ui.text_status.insert(END, "성공적으로 저장하였습니다. (파일이름: "+self.fileName+")")

    def inFile(self):
        self.ui.clear_status()
        self.fileName = self.ui.entry_list[8].get().strip()
        if self.fileName == "":
            self.ui.text_status.insert(END, "[읽기 실패] 파일이름이 공백 입니다.")
            return
        try:
            f = open("./" + self.fileName + ".txt", 'r')
        except:
            self.ui.text_status.insert(END, "[읽기 실패] 존재하지 않는 파일입니다.")
            return

        self.datahandler.data_dic.clear()
        lines = f.readlines()
        for line in lines:
            self.elems = line.strip().split("\t")
            self.datahandler.data_dic[eval(self.elems[0])] = [self.elems[1], eval(self.elems[2])]
        f.close()
        self.ui.update_text()
        self.ui.entry_list[8].delete(0, END)
        self.ui.text_status.insert(END, "성공적으로 파일을 읽었습니다. (파일이름: " + self.fileName + ")")
