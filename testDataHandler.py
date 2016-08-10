#-*- coding: utf-8 -*-
import unittest

class TestDataHandler(unittest.TestCase):
    def setIndex(self,dic):
        self.data_dic = dic
        self.temp_idx = 1
        for k,v in self.data_dic.items():
            if k == self.temp_idx:
                self.temp_idx += 1
        self.index =self.temp_idx
        return self.index

    def add(self,Name,Score,dic):
        self.data_dic = dic

        self.name = Name.strip()
        if self.name == "":
            print "[추가 실패] 이름란이 공백 입니다."
            return False

        try:
            self.score = eval(Score)
        except:
            print "[추가 실패] 점수를 정확히 입력하세요."
            return False

        for k,v in self.data_dic.items():
            if v[0] == self.name :
                print "[추가 실패] 동일한 이름이 이미 존재합니다."
                return False

        self.index = self.setIndex(dic)
        self.data_dic[self.index] = [self.name,eval(Score)]
        print "성공적으로 추가하였습니다"
        print self.data_dic
        return True

    def delete(self,Number,DIC):

        try:
            self.number = eval(Number)
        except:
            print "[삭제 실패] 정확한 번호를 입력하세요."
            return False

        self.hasNum = False
        self.data_dic = DIC
        for k,v in self.data_dic.items():
            if k == self.number :
                self.hasNum = True
                break

        if not self.hasNum:
            print "[삭제 실패] 존재하지 않는 번호입니다."
            return False

        else:
            self.data_dic.pop(self.number)
            print "성공적으로 제거하였습니다."
            print self.data_dic
            return True

    def sortName(self,DIC):
        self.data_dic = DIC
        self.name_sorted = sorted(self.data_dic.items(),key = lambda x:x[1][0])
        self.name_list = []
        for elems in self.name_sorted:
            self.name_list.append(elems[1][0])

        for idx in range(len(self.name_list)-1):
            if self.name_list[idx] > self.name_list[idx+1]:
                print "정렬실패(이름순)"
                return False
        print "정렬성공(이름순)"
        print self.name_sorted
        return True

    def sortScore(self,DIC):
        self.data_dic = DIC
        self.score_sorted = sorted(self.data_dic.items(),key = lambda x:x[1][1],reverse=True)
        self.score_list = []
        for elems in self.score_sorted:
            self.score_list.append(elems[1][1])

        for idx in range(len(self.score_list)-1):
            if self.score_list[idx] < self.score_list[idx+1]:
                print "정렬실패(점수순)"
                return False
        print "정렬성공(점수순)"
        print self.score_sorted
        return True

    def sortScore_REV(self,DIC):
        self.data_dic = DIC
        self.score_sorted = sorted(self.data_dic.items(), key=lambda x: x[1][1])
        self.score_list = []
        for elems in self.score_sorted:
            self.score_list.append(elems[1][1])

        for idx in range(len(self.score_list) - 1):
            if self.score_list[idx] > self.score_list[idx + 1]:
                print "정렬실패(점수역순)"
                return False
        print "정렬성공(점수역순)"
        print self.score_sorted
        return True

    def test_SetIndexAndAdd(self):
        self.temp_dic = {1:["test1",50],2:["2test",70],5:["i'm test",100]}
        self.assertEqual(3,self.setIndex(self.temp_dic))
        print "\n--------------------- 인덱스 테스트 종료 --------------------------"
        self.assertFalse(self.add("\t","77",self.temp_dic))
        self.assertFalse(self.add("test1","77",self.temp_dic))
        self.assertTrue(self.add("unitTest","89",self.temp_dic))
        print "----------------------- 추가 테스트 종료 ---------------------------"

    def test_delete(self):
        self.temp_dic = {1: ["test1", 50], 2: ["2test", 70], 5: ["i'm test", 100]}
        self.assertFalse(self.delete(" ", self.temp_dic))
        self.assertFalse(self.delete("9", self.temp_dic))
        self.assertTrue(self.delete("2", self.temp_dic))
        print "----------------- ----- 삭제 테스트 종료 ---------------------------"

    def test_sortName(self):
        self.temp_dic = {1: ["test1", 50], 2: ["2test", 70], 5: ["i'm test", 100]}
        self.assertTrue(self.sortName(self.temp_dic))
        print "----------------- 이름순 정렬 테스트 종료 ---------------------------"

    def test_sortScore(self):
        self.temp_dic = {1: ["test1", 50], 2: ["2test", 70], 5: ["i'm test", 100]}
        self.assertTrue(self.sortScore(self.temp_dic))
        print "--------------- 점수내림차순 정렬 테스트 종료 ------------------------"


    def test_sortScore_REV(self):
        self.temp_dic = {1: ["test1", 50], 2: ["2test", 70], 5: ["i'm test", 100]}
        self.assertTrue(self.sortScore_REV(self.temp_dic))
        print "--------------- 점수오름차순 정렬 테스트 종료 -----------------------"

if __name__ == "__main__":
    unittest.main()