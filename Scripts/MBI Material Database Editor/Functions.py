'''
Created on 27.04.2020

@author: Felix Steinbach
'''

def stringTo2DList(string):
    list1=[n.replace('    ',';').split(';') for n in string.rstrip().split('\n')]
    return [list(a) for a in zip(*list1)]


def stringTo2DIntList(string):
    list1=[n.replace('    ',';').split(';') for n in string.rstrip().split('\n')]
    list2=[list( map(float,i) ) for i in list1]
    return [list(a) for a in zip(*list2)]

def stringToList2(string):
    list1=string.rstrip().split('\n')  
    return list1

def stringToList(string):
    list1=string.rstrip().replace('    ',';').split(';')
    return list1

def listToString(list1,sep):
    return sep.join(list1)

def List2DToString(list1,sep):
    list2=[list(a) for a in zip(*list1)]
    return "\n".join([sep.join(i) for i in list2])

def intList2DToString(list1,sep):
    list2=[list(a) for a in zip(*list1)]
    list3=[list( map(str,i) ) for i in list2]
    return "\n".join([sep.join(i) for i in list3])

