# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VmUdpKiLUpIcBn8sNAbDDlX8o1o0tXCC
"""

"""
Created on Mon Feb 28 19:40:41 2022

@author: Mumu
"""
import math
print("1.Addition\n2.Substractor\n3.Multiplication\n4.Division")
print("5.Sin\n6.Cos\n7.tan\n8.ln\n9.log_base\n10.Power\n11.Square_root\n12.squareroot of n\13.power exponent\n14.percentage")
option=int(input("Choose an option:"))
if option==1:
  print("How many variables you want to take")
  n=int(input("\nTake inputs: "))
  if n==2:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    add=num1+num2
  if n==3:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    add=num1+num2+num3
  if n==4:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    num4=float(input("Num4: "))
    add=num1+num2+num3+num4
  print("The addition of number is: ",add)

elif option==2:
  print("How many variables you want to take")
  n=int(input("\nTake inputs: "))
  if n==2:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    sub=num1-num2
  if n==3:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    sub=num1-num2-num3
  if n==4:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    num4=float(input("Num4: "))
    sub=num1-num2-num3-num4
  print("The subtraction of number is: ",sub)

elif option==3:
  print("How many variables you want to take")
  n=int(input("\nTake inputs: "))
  if n==2:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    mul=num1*num2
  if n==3:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    mul=num1*num2*num3
  if n==4:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    num4=float(input("Num4: "))
    mul=num1*num2*num3*num4
  print("The multiplication of number is: ",mul)

elif option==4:
  print("How many variables you want to take")
  n=int(input("\nTake inputs: "))
  if n==2:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    div=num1/num2
  if n==3:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    div=num1/num2/num3
  if n==4:
    num1=float(input("Num1: "))
    num2=float(input("Num2: "))
    num3=float(input("Num3: "))
    num4=float(input("Num4: "))
    div=num1/num2/num3/num4
  print("The division of number is: ",div)

elif option== 5:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        print("1.Degree\n2.Radian")
        n1=int(input())
        if n1==1:
            ans=math.sin(num1)
        if n1==2:
            ans=math.sin(math.radians(num1))
    print("Ans",ans)

elif option== 6:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        print("1.Degree\n2.Radian")
        n1=int(input())
        if n1==1:
            ans=math.cos(num1)
        if n1==2:
            ans=math.cos(math.radians(num1))
    print("Ans",ans)
    
elif option== 7:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        print("1.Degree\n2.Radian")
        n1=int(input())
        if n1==1:
            ans=math.tan(num1)
        if n1==2:
            ans=math.tan(math.radians(num1))
    print("Ans",ans)   
    
elif option== 8:
    print("How many variables you want to take ")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        Ans=math.log(num1)
    print("Ans",ans)
    
elif option== 9:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        base=int(input("Base number:"))
        Ans=math.log(num1,base)
    print("Ans",ans)
    
elif option== 10:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 2:
        num1=float(input("Number1: "))
        num2=float(input("Number2: "))
        Ans=num1**num2
    if n== 3:
        num1=float(input("Number1: "))
        num2=float(input("Number2: "))
        num3=float(input("Number3: "))
        Ans=num1**num2*num3
    print("Ans",ans)
    
elif option== 11:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        Ans=math.sqrt(num1)
    print("Ans",ans)

elif option== 12:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        base=int(input("Base number:"))
        Ans=math.sqrt(num1,base)
    print("Ans",ans)
    
elif option== 13:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        base=int(input("Base number:"))
        Ans=pow(num1,base)
    print("Ans",ans)
    
elif option== 14:
    print("How many variables you want to take")
    n=int(input("\nTake inputs: "))
    if n== 1:
        num1=float(input("Number1: "))
        Ans=num1/100
    print("Ans",ans)

else:
    print("Invalid input")
