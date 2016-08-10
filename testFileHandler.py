#-*- coding: utf-8 -*-
import unittest

class TestFileHandler(unittest.TestCase):

    def outFile(self,FileName,dictionary):
        self.fileName = FileName.strip()
        if self.fileName == "":
            print "[저장 실패] 파일이름이 공백 입니다."
            return False

        f = open("./" + self.fileName + ".txt", 'w')
        for k, v in dictionary.items():
            f.write(str(k) + "\t" + v[0] + "\t" + str(v[1]) + "\n")
        f.close()
        self.FileName = ""
        print "성공적으로 저장하였습니다. (파일이름: " + self.fileName + ")"
        return True

    def inFile(self,FileName):
        self.fileName = FileName.strip()
        if self.fileName == "":
            print "[읽기 실패] 파일이름이 공백 입니다."
            return False

        try:
            f = open("./" + self.fileName + ".txt", 'r')
        except:
            print "[읽기 실패] 존재하지 않는 파일입니다."
            return False

        self.data_dic = {}
        lines = f.readlines()
        for line in lines:
            self.elems = line.strip().split("\t")
            self.data_dic[eval(self.elems[0])] = [self.elems[1], eval(self.elems[2])]

        f.close()
        print "성공적으로 파일을 읽었습니다. (파일이름: " + self.fileName + ")"
        print "읽은 데이터 딕셔너리"
        print self.data_dic
        return True


    def testOutFile(self):
        self.assertFalse(self.outFile(" ",{1:["test1",50],2:["2test",70],5:["i'm test",100]}))
        self.assertTrue(self.outFile("fileHandler_unittest", {1: ["test1", 50], 2: ["2test", 70], 5: ["i'm test", 100]}))


    def testInFile(self):
        self.assertFalse(self.inFile("\n"))
        self.assertTrue(self.inFile("fileHandler_unittest"))

if __name__ == "__main__":
    unittest.main()