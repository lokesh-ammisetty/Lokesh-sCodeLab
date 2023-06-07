#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:26:00 2023

@author: lokesh
"""

####                              DATA TYPES                      ####
#none
#Numerics
#Sequences
#sets
#Mappings

####_________[NONE]____________###########
## 1) none:- (None)
a=None
type(a)



####_________[NUMERIC]_________###########
## 1)int:-
a=5
b=0
c=-1
d=c*a
type(a)
type(b)
type(c)
type(d)
## 2)float:-
f1=0.0000
f2=1.0
f3=a/c
type(f1)
type(f2)
type(f3)
## 3)complex:-
c1=1+1j
c2=4+5j
c3=0+0j
C=c1+c2
type(C)
type(c1)
type(c2)
type(c3)




#####_________[SEQUENCES]_________###########
## 1) String (str)
s="a"
s1="shiva"
s2='siva'
s3="9"
s4="9491366901"
s5="@paytm"
type(s)
type(s1)
type(s2)
type(s3)
type(s4)
type(s5)

## 2) list:-
l=[1,2,3,4,5]
l1=['lokesh','krishna','ravi','mahesh']
l2=[70.0,3,9.0,4/2,0,"siva",70.0]
type(l)
type(l1)
type(l2)
l2

## 3) tupple:-
t=(1,2,3,4,5)
t1=('lokesh','mahesh','ravi','krishna')
t2=(70.0,3,9.0,4*2,0,"siva",0)
type(t)
type(t1)
type(t2)
t2

## 4) range:-
r=range(0,10)
r1=range(-10,-1)
r2=list(range(0,100))
type(r)
type(r1)
type(r2)
r
r1
r2
list(r1)
list(r)



####___________[SETS]____________########
## 1) sets:-
st={'a','b','c',"lokesh",69,45.0,0,0,1+4j,False,True,1,1}
type(st)
st
st1={'babu','chai','teja','sai'}
## 2) frozen sets
st1=frozenset(st)
st1
st
 

####____________[MAPPINGS]________#######
## 1) dictionarys
d={1001:'a',1002:'b',1003:'c',1004:0,1005:True,1006:False}
type(d)
d
d1={'lokesh':56,'krishna':74,'ravi':69,'sai':90}
#_______________________________XXX_________________________________________#

#####___________________________SLICING________________________________#####
#Slicing :- extraction of particular element or character or set of character.
         #slicing can only done on strings,list,tupple,bytes,bytearrays,range.
         #can be performed only on types having index numbers
         #it has +ve and -ve indexing 
         #+ve starts with 0
         #-ve starts with -1
l1[1]       
l1[0:5]
l1[:]
l1[5::-1]
s4[0::2]
s4[-1:-11:-1]
first_half_number=s4[0:5]
second_half_number=s4[5:]
first_half_number
second_half_number
print('first_half_number',s4[0:5])

####_____________________concadination_______________############
## used to join two strings, can not be performed on numerics.
  # symbole used (+)
  # concadination can not be performed on sets and dictionarys
upi = s4+s5
upi
lc=l1+l2
lc
tc=t1+t2
tc
sc=st+st1 # error
dc=d+d1   #error

####_____________________repeating___________________#############
## used to repete strings and other data types
  # symbol used(*)
  # can not be performed on sets and dictionarys
rs=s4*4
rs
rl=l1*4
rl
rt=t1*4
rt
sr=st*4 #error
sr
rd=d*4  #error
rd


####____________________operators______________________#############
## Arithmatic
## Assignment
## comparision
## Logical
## Identity 
## Bitwise
## Membership
## Boolean
## Unary

####____________________Arithmatic operatiors__________#############
## (+) used to add two numerics 
40+20
40.0+20
1+2j + 20

## (-) used to substact two numerics
40-20
40.0-20
1+2j-20

## (*) used to multiply two numerics
40*20
40.0*20
(1+2j) *20

## (/) used to divide two numerics
40/20
20/40

## (%) called as modulo division, gives reminder or numerator
  # frequently used for getting last digit(%10)
40%20
20%40
1234%10

## (**) exponent operator, acts as power 
2**5
5**3

## (//) used to get quotient
40//20
20//40
40//10
440//10













































































































