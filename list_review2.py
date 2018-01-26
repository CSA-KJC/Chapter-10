#Katie Chiu
#Computer Programming 12th
#January 22, 2018

import random

def lists():
    myList=[]
    list1=[76]
    list2=[92.3]
    list3=["hello"]
    list4=[True]
    list5=[4]
    list6=[76]
    myList=myList+list1+list2+list3+list4+list5+list6
    print(myList)
    myList=[]
    myList.append(76)
    myList.append(92.3)
    myList.append("hello")
    myList.append(True)
    myList.append(4)
    myList.append(76)
    print(myList)
    
def integer():
    newlist=[]
    for y in range(100):
        prob=random.random()
        x=random.randrange(0, 1001)
        newlist.append(x)
    print(newlist)
    return newlist

def average(newlist):
    add=0
    for x in newlist:
        add=add+x
    add=add/100
    print(add)
    return add

lists()
newlist=integer()
average(newlist)
