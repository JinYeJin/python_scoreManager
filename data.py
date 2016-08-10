#-*- coding: utf-8 -*-
from Tkinter import *

class DataHandler:
    def __init__(self,UI):
        self.ui = UI
        self.data_dic ={}
        self.index = 0

    def setIndex(self):
        self.temp_idx = 1
        for k,v in self.data_dic.items():
            if k == self.temp_idx:
                self.temp_idx += 1
        self.index =self.temp_idx

    def add(self):
        self.ui.clear_status()

        self.name = self.ui.entry_list[0].get().strip()
        if self.name == "":
            self.ui.text_status.insert(END,"[추가 실패] 이름란이 공백 입니다.")
            return

        try:
            self.score = eval(self.ui.entry_list[1].get())
        except:
            self.ui.text_status.insert(END, "[추가 실패] 점수를 정확히 입력하세요.")
            return

        for k,v in self.data_dic.items():
            if v[0] == self.name :
                self.ui.text_status.insert(END, "[추가 실패] 동일한 이름이 이미 존재합니다.")
                return


        self.setIndex()
        self.data_dic[self.index] = [self.name,eval(self.ui.entry_list[1].get())]
        self.ui.entry_list[0].delete(0, END)
        self.ui.entry_list[1].delete(0, END)
        self.ui.update_text()
        self.ui.text_status.insert(END, "성공적으로 추가하였습니다")

    def delete(self):
        self.ui.clear_status()

        try:
            self.number = eval(self.ui.entry_list[2].get())
        except:
            self.ui.text_status.insert(END, "[삭제 실패] 정확한 번호를 입력하세요.")
            return

        self.hasNum = False
        for k,v in self.data_dic.items():
            if k == self.number :
                self.hasNum = True
                break

        if not self.hasNum:
            self.ui.text_status.insert(END, "[삭제 실패] 존재하지 않는 번호입니다.")
            return

        else:
            self.data_dic.pop(self.number)
            self.ui.entry_list[2].delete(0, END)
            self.ui.update_text()
            self.ui.text_status.insert(END, "성공적으로 제거하였습니다.")

    def changeName(self):
        self.ui.clear_status()

        try:
            self.number = eval(self.ui.entry_list[3].get())
        except:
            self.ui.text_status.insert(END, "[수정 실패] 올바른 번호를 입력해주세요.")
            return

        self.hasNum = False
        for k,v in self.data_dic.items():
            if k == self.number:
                self.hasNum = True
                break
        if self.hasNum == False:
            self.ui.text_status.insert(END, "[수정 실패] 존재하지 않는 번호입니다.")
            return

        self.name = self.ui.entry_list[4].get().strip()
        if self.name == "":
            self.ui.text_status.insert(END, "[수정 실패] 이름란이 공백입니다.")
            return

        for k,v in self.data_dic.items():
            if v[0] == self.name :
                self.ui.text_status.insert(END, "[추가 실패] 동일한 이름이 이미 존재합니다.")
                return

        self.data_dic[self.number] = [self.name,self.data_dic[self.number][1]]

        self.ui.entry_list[3].delete(0, END)
        self.ui.entry_list[4].delete(0, END)
        self.ui.update_text()
        self.ui.text_status.insert(END, "이름을 수정하였습니다.")

    def changeScore(self):
        self.ui.clear_status()

        try:
            self.number = eval(self.ui.entry_list[5].get())
        except:
            self.ui.text_status.insert(END, "[수정 실패] 올바른 번호를 입력해주세요.")
            return

        self.hasNum = False
        for k,v in self.data_dic.items():
            if k == self.number:
                self.hasNum = True
                break
        if self.hasNum == False:
            self.ui.text_status.insert(END, "[수정 실패] 존재하지 않는 번호입니다.")
            return

        try:
            self.score = eval(self.ui.entry_list[6].get())
        except:
            self.ui.text_status.insert(END, "[수정 실패] 올바른 점수를 입력해주세요.")
            return

        self.data_dic[self.number] = [self.data_dic[self.number][0],self.score]

        self.ui.entry_list[5].delete(0, END)
        self.ui.entry_list[6].delete(0, END)
        self.ui.update_text()
        self.ui.text_status.insert(END, "점수를 수정하였습니다.")

    #There is no algorithm, Just reprint
    def sortIndex(self):
        self.ui.clear_status()
        self.ui.update_text()

    def sortName(self):
        self.ui.clear_status()
        self.name_sorted = sorted(self.data_dic.items(),key = lambda x:x[1][0])
        self.ui.text_data.delete("1.0", END)
        for elems in self.name_sorted:
            self.ui.text_data.insert(END,str(elems[0])+"\t"+elems[1][0]+"\t"+str(elems[1][1])+"\n")

    def sortScore(self):
        self.ui.clear_status()
        self.score_sorted = sorted(self.data_dic.items(), key=lambda x: x[1][1], reverse=True)
        self.ui.text_data.delete("1.0", END)
        for elems in self.score_sorted:
            self.ui.text_data.insert(END, str(elems[0]) + "\t" + elems[1][0] + "\t" + str(elems[1][1]) + "\n")

    def sortScore_REV(self):
        self.ui.clear_status()
        self.score_sorted = sorted(self.data_dic.items(), key=lambda x: x[1][1])
        self.ui.text_data.delete("1.0", END)
        for elems in self.score_sorted:
            self.ui.text_data.insert(END, str(elems[0]) + "\t" + elems[1][0] + "\t" + str(elems[1][1]) + "\n")
