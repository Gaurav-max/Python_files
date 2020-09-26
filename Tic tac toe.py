# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:47:44 2020

@author: gaurav balodi
"""
import pandas as pd
#import numpy as np
from numpy import *
from tkinter import *
import sys

master=Tk()
Label(master,text=' tic tak toe').grid(row=1,column=1)
Label(master,text=' enter button of your choice').grid(row=2,column=1)


li=['_','_','_','_','_','_','_','_','_']
print(li[0],'|',li[1],'|',li[2],'\n',
      li[3],'|',li[4],'|',li[5],'\n',
      li[6],'|',li[7],'|',li[8])


def winner():
        if li[0]==li[1]==li[2]=="X" or li[3]==li[4]==li[5]=="X":
            print("pr1 is winner")
            e1.insert("pr1 is winner")
            sys.exit()
        elif li[6]==li[7]==li[8]=="X" or li[0]==li[3]==li[6]=="X":
            print("pr1 is winner")
            e1.insert("pr1 is winner")
            sys.exit()
        elif li[1]==li[4]==li[7]=="X" or li[2]==li[5]==li[8]=="X":
            print("pr1 is winner")
            e1.insert("pr1 is winner")
            sys.exit()
        elif li[0]==li[4]==li[8]=="X" or li[2]==li[4]==li[6]=="X":
            print("pr1 is winner ")
            e1.insert("pr1 is winner")
            sys.exit()
        elif li[0]==li[1]==li[2]=="o" or li[3]==li[4]==li[5]=="o":
            print("pr2 is winner")
            sys.exit()
        elif li[6]==li[7]==li[8]=="o" or li[0]==li[3]==li[6]=="o":
            print("pr2 is winner")
            sys.exit()
        elif li[1]==li[4]==li[7]=="o" or li[2]==li[5]==li[8]=="o":
            print("pr2 is winner")
            sys.exit()
        elif li[0]==li[4]==li[8]=="o" or li[2]==li[4]==li[6]=="o":
            print("pr2 is winner ")
            sys.exit()

def dual():
    global a
    a=0
    
    while a<9:
        a+=1
        
        def pr1():
            x=int(input('pr1 enter your move'))
            if x>9:
                print('enter the no b/w 0 to 9')
                return(pr1())
            elif li[x-1]!="_":
                print("space occupiued")
                return(pr1())
            else :
                li[x-1]='X'
                print(li[0],'|',li[1],'|',li[2],'\n',
                      li[3],'|',li[4],'|',li[5],'\n',
                      li[6],'|',li[7],'|',li[8])
                winner()
                
        pr1() #calling pr1 fun ction
        print("chances played ",a)
        def pr2():
            x=int(input('pr2 enter your move'))
            if x>9:
                print('enter the no b/w 0 to 9')
                return(pr2())
            elif li[x-1]!="_":
                print("space occupiued")
                return(pr2())
            else :
                
                li[x-1]='o'
                print(li[0],'|',li[1],'|',li[2],'\n',
                      li[3],'|',li[4],'|',li[5],'\n',
                      li[6],'|',li[7],'|',li[8]) 
                winner()
    
        a+=1
        if a>9:
            print("__DRAW__")
            break
            
        
        pr2() #calling pr2 function '''
        print("chances played",a)


def CPU():
    global a
    a=0
    while a<9:
        a+=1
        
        def pr1():
            x=int(input('pr1 enter your move   '))
            if x>9:
                print('enter the no b/w 0 to 9 \n')
                return(pr1())
            elif li[x-1]!="_":
                print("space occupiued")
                return(pr1())
            else :
                li[x-1]='X'
                print(li[0],'|',li[1],'|',li[2],'\n',
                      li[3],'|',li[4],'|',li[5],'\n',
                      li[6],'|',li[7],'|',li[8])
                winner()
                
        pr1() #calling pr1 fun ction
        print("move made by pr1 \n")
        print("chances played ",a)
        def pr2():
            
            y=int(ceil(10*random.random()))
            if y>9:
                print('enter the no b/w 0 to 9 \n')
                return(pr2())
            elif li[y-1]!="_":
                print("space occupiued \n")
                return(pr2())
            else :
                
                li[y-1]='o'
                print(li[0],'|',li[1],'|',li[2],'\n',
                      li[3],'|',li[4],'|',li[5],'\n',
                      li[6],'|',li[7],'|',li[8]) 
                winner()
    
        a+=1
        if a>9:
            print('__DRAW__')
            break
        
        pr2() #calling pr2 function 
        print("move made by pr2 \n")
        print("chances played",a)


Button(master,text='dual',command=dual).grid(row=3,column=1)
Button(master,text='CPU',command=CPU).grid(row=4,column=1)
master.mainloop()