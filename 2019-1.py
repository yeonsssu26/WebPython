import csv
#import os

class myFile:
    def __init__(self, _fileName = None, _fileMode = None): #1
        self.status = True
        self.fMat = []
        #self.path = os.getcwd()+'\\'+_fileName
        #print(self.path)
        #self.path = '.\\'+_fileName

        if (_fileMode == 'r'):
            self.f = open(_fileName, 'r')
            
            r = csv.reader(self.f)
            for line in r:
                self.fMat.append(line)

            sortById = self.fMat[1:]
            sortById.sort(key = lambda x : x[0])
            self.fMat[1:] = sortById

        elif(_fileMode == 'w'):
            #self.f = open(self.path, 'w')
            self.f = open(_fileName, 'w')

        else:
            self.status = False
            print("error.1")


    def getStatus(self): #2
        if (self.status == False):
            print("error.2")
        return self.status

    def getBody(self): #3
        if (self.status == True):
            self.body = self.fMat[1:]
            return self.body
        else:
            print("error.3")
            return False

    def setContentHead(self, _head = None): #4
        if (self.status == True) and (_head is not None):
            self.head = _head
        else:
            print("error.4")
        return self.status

    def setContentBody(self, _body = None): #5
        if (self.status == True) and (_body is not None):
            self.body = _body
        else:
            print("error.5")
        return self.status

    def writeFile(self): #6
        if (self.status == True):
            row = ','.join(self.head)+'\n'
            self.f.write(row)
            for i in range(len(self.body)):
                row = ','.join(self.body[i])+'\n'
                self.f.write(row)
        else:
            print("error")
        return self.status

    def closeFile(self): #7
        if (self.status == True):
            self.f.close()
        else:
            print("error.7")
        return self.status        

    def mergeList(self, _list1, _list2): #8
        self.afterMerge = []

        for i in range(len(_list1)):
            for j in range(len(_list2)):
                if(_list1[i][0] == _list2[j][0]):
                    row = _list1[i] + _list2[i][1:]

                    avg = round((int(_list2[i][1]) + int(_list2[i][2]) + int(_list2[i][3])) / 3)
                    row = _list1[i] + _list2[i][1:] + [str(avg)]

                    self.afterMerge.append(row)
        self.body = self.afterMerge
        return self.body
    
file1 = myFile("inputdata1.csv", 'r')
file2 = myFile("inputdata2.csv", 'r')

if (file1.getStatus() != False) and (file2.getStatus() != False):
    file3 = myFile("output.csv", 'w')
    file3.setContentHead(["ID", "Name", "Course 1", "Course 2", "Course 3", "Average"])

    print(file1.getBody())
    print(file2.getBody())

    file3.mergeList(file1.getBody(), file2.getBody())
    
    file3.writeFile()
    file3.closeFile()
else:
    print("input file error")

file1.closeFile()
file2.closeFile()
