#-*- coding: utf-8 -*-
from Tkinter import *


class UI:
    def __init__(self,main):
        self.frame_top = Frame(main)
        self.frame_top.grid(row=0,column=0,sticky=N)
        self.frame_top.configure(bg="white")

        self.label_list = ["이름","번호","번호","점수","번호","이름","점수","파일이름","파일이름"]
        r=0;c=0
        for label in self.label_list:
            Label(self.frame_top,text=label,bg="white").grid(row=r,column=c,sticky=E)
            if c==0:
                if r==0:
                    r=2
                    continue
                elif r==2:
                    r=3
                    continue
                else:
                    c=2
                    r=0
                    continue
            r+=1

        self.entry_list = []
        self.entry_width = [20,7,5,5,20,5,7,20,20]
        r=0;c=1;i=0
        for width in self.entry_width:
            if i<3:
                self.bg_color = "light green"
            elif i<7:
                self.bg_color = "light gray"
            else:
                self.bg_color = "light blue"

            self.entry_list.append(Entry(self.frame_top,width=width,bg=self.bg_color))
            self.entry_list[i].grid(row=r,column=c,sticky=W)
            i+=1

            if i==1:
                c+=2
            elif i==2:
                r=1
            elif i==3:
                r=2;c=1
            elif i==4:
                c+=2
            elif i==5:
                r=3;c=1
            elif i==6:
                c+=2
            else:
                r+=1


        self.frame_mid = Frame(main)
        self.frame_mid.grid(row=1,column=0,sticky=N)
        self.frame_mid.configure(bg="white")

        self.frame_btm = Frame(main)
        self.frame_btm.grid(row=2,column=0,sticky=N)
        self.frame_btm.configure(bg="white")

        self.text_data = Text(self.frame_btm,width=75,height=10,bg="light yellow")
        self.text_data.grid(row=0,column=0,sticky=N)
        self.text_status = Text(self.frame_btm,width=75,height=1,bg="pink")
        self.text_status.grid(row=1,column=0,sticky=N)

    def init_btn(self,dataHandler,fileHander):
        self.datahandler = dataHandler
        self.filehandler = fileHander

        self.btn_add = Button(self.frame_top, text="추가", width=5, command=self.datahandler.add, bg="white",highlightbackground="white",activebackground="white")
        self.btn_add.grid(row=0, column=4, sticky=W)

        self.btn_delete = Button(self.frame_top, text="삭제", width=5, command=self.datahandler.delete, bg="white", highlightbackground="white",activebackground="white")
        self.btn_delete.grid(row=1, column=4, sticky=W)

        self.btn_change_name = Button(self.frame_top, text="수정", width=5, command=self.datahandler.changeName, bg="white",highlightbackground="white",activebackground="white")
        self.btn_change_name.grid(row=2, column=4, sticky=W)

        self.btn_change_score = Button(self.frame_top, text="수정", width=5, command=self.datahandler.changeScore, bg="white", highlightbackground="white",activebackground="white")
        self.btn_change_score.grid(row=3, column=4, sticky=W)

        self.btn_save = Button(self.frame_top, text="저장", width=5, command=self.filehandler.outFile, bg="white",highlightbackground="white", activebackground="white")
        self.btn_save.grid(row=4, column=4, sticky=W)

        self.btn_open = Button(self.frame_top, text="열기", width=5, command=self.filehandler.inFile, bg="white",highlightbackground="white", activebackground="white")
        self.btn_open.grid(row=5, column=4, sticky=W)

        self.btn_num_sort = Button(self.frame_mid,text="번호순",width=5, command=self.datahandler.sortIndex,bg="white",highlightbackground="white",activebackground="white")
        self.btn_num_sort.grid(row=0,column=0,sticky=N)

        self.btn_name_sort = Button(self.frame_mid,text="이름순",width=5, command=self.datahandler.sortName,bg="white",highlightbackground="white",activebackground="white")
        self.btn_name_sort.grid(row=0,column=1,sticky=N)

        self.btn_downscore = Button(self.frame_mid,text="점수내림차순",width=15, command=self.datahandler.sortScore,bg="white",highlightbackground="white",activebackground="white")
        self.btn_downscore.grid(row=0,column=2,sticky=N)

        self.btn_upscore = Button(self.frame_mid,text="점수오름차순",width=15, command=self.datahandler.sortScore_REV,bg="white",highlightbackground="white",activebackground="white")
        self.btn_upscore.grid(row=0,column=3,sticky=N)

    def clear_status(self):
        self.text_status.delete("1.0",END)

    def update_text(self):
        self.text_data.delete("1.0", END)
        for k,v in self.datahandler.data_dic.items():
            self.text_data.insert(END, k)
            self.text_data.insert(END, "\t" + v[0] + "\t")
            self.text_data.insert(END, v[1])
            self.text_data.insert(END, "\n")