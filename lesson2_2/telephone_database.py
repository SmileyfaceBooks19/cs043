 # telephone directory DATABASE
import os

class Simpledb:
    def __init__(self,file):
        self.file = file

    def add(self,name,num):
        self.name = name
        self.num = num
        f = open(self.file,'w')
        f.write('%s\t%s\n' %(self.name, self.num))
        f.close()

    def find(self,name):
        self.name = name
        f = open(self.file,'r')
        for line in f:
            (k, v) = line.split('\t')
            if k == self.name:
                return v[:-1]
            else:
                print('The entry was not found.')
        f.close()

    def delete(self,name):
        self.name = name
        f = open(self.file,'r')
        n = open('result.txt','w')
        inTxt = False
        for line in f:
            (k, v) = line.split()
            if k != self.name:
                 n.write(line)
            else:
                inTxt = True
        if inTxt == False:
            print('The entry was not found.')
        return inTxt
        f.close()
        n.close()
        os.replace('result.txt',self.file)

    def update(self,name,num):
        self.name = name
        self.num = num
        f = open(self.file,'r')
        n = open('result.txt','w')
        inTxt = False
        for line in f:
            (k, v) = line.split('\t')
            if k == name:
                n.write('%s\t%s\n' %(self.name,self.num))
                inTxt = True
            elif k != self.name:
                n.write(line)
        if inTxt == False:
            print('The entry was not found.')
        return inTxt
        f.close()
        n.close()
        os.replace('result.txt',self.file)
