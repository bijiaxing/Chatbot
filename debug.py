# -*- coding: UTF-8 -*-

def readQSresouce(path,list1,list2):  # read top n word vectors
    with open(path) as f:
        tag=True
        for line in f:
            if tag==True:
                list1.append(line)
                tag=False
            else:
                list2.append(line)
                tag=True
    return
list1=[]
list2=[]

readQSresouce('wordresource.txt',list1,list2)
print(list1)
print(list2)
