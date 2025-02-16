#A Quick Review of PYTHON--------------------------------------------------------------------------------------

#Here are some easy python example. Enjoy them :)

#Check an input number is Even or Odd--------------------------------------------------------------------------

# number=float(input("Please enter a number: "))
# print(number, ' is a good choice')
# if number%2==0:
#     print(number, ' is Even!!!')
# else:
#     print(number, ' is Odd!!!')

#Chech an input number is Positive, Negative or Zero-----------------------------------------------------------

# number=float(input("Please enter a number: "))
# print(number, ' is a good choice')
# if number>0:
#     print(number, ' is Positive :)')
# elif number<0:
#     print(number, ' is Negative :)')
# else:
#     print(number, ' is Zero :0')

#Swap two variable---------------------------------------------------------------------------------------------

#Using third Variable like "temp"*****
# first=1
# second=2
# print('The First Variable Value is: "',first,'" and the Second Variable Value is: "', second,'"')
# temp=first
# first=second
# second=temp
# print('Now, The First Variable Value is: "',first,'" and the Second Variable Value is: "', second,'"')

#Using third Variable*****
# first=1
# second=2
# print('The First Variable Value is: "',first,'" and the Second Variable Value is: "', second,'"')
# first+=second
# second=first-second
# first=first-second
# print('Now, The First Variable Value is: "',first,'" and the Second Variable Value is: "', second,'"')

#Assign a Grade to a Score-------------------------------------------------------------------------------------------------
"""Take a Score input from user, assign a Grade based on th score:
        * 90-100: Grade A
        * 80-90: Grade B
        * 70-80: Grade C
        * 60-70: Grade D
        * Below 60: Fail
"""

# score=float(input("Please enter a score: "))
# if score>100 or score<0:
#     print('invalid score!!! please enter a valid score between 0 to 100')
# else:
#     if 90<=score<=100:
#         print('Grade A')
#     elif 80<=score<90:
#         print('Grade B')
#     elif 70<=score<80:
#         print('Grade C')
#     elif 60<=score<70:
#         print('Grade D')
#     else:
#         print('Sorry, Fail :(')

#Calculate some of Even value from zero to upper limit user value---------------------------------------------

# number=int(input("Please enter a limit value: "))

# if number<0:
#     print('please enter a positive value')
# else:
#     i=sum=0
#     while(i<=number):
#         i+=1
#         if i%2!=0:
#             sum+=i
#     print(sum)

#Multiples of a number from 1 to 100; for example for number=40, the answer is 120=40+80---------------------

# number=float(input("Please enter a number: "))
# sum=0
# if 0<=number<=100:
#     for i in range(101):
#         if i%number==0:
#             sum+=i
#     print(sum)
# else:
#     print('Please enter a value berween 0 to 100')

#Convert celsius temprator to fahrenheit---------------------------------------------------------------------

# celsius=float(input("Please enter a temprator: "))
# farenheit=(celsius*9.5)+32
# print(celsius, ' celsius is ',farenheit, ' farenheit')

#Print this shap:
"""
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""
# n=5
# for i in range (1,6):
#     print((n-i)*' ',i*('* '))
# for i in range (4,0,-1):
#     print((n-i)*' ',i*('* '))

#HOP game with user input-------------------------------------------------------------------------------------

# limit=int(input('Please enter the limit value: '))
# hop=int(input('Please enter the HOP value: '))
# i=0
# while(i<=limit):
#     if i%hop==0:
#         print("HOP")
#     else:
#         print(i,end=" ")
#     i+=1

#Determine the type of a triangle based of the size of its sides ----------------------------------------------

# firstSide=float(input('Please enter the first side size: '))
# secondSide=float(input('Please enter the second side size: '))
# thirdSide=float(input('Please enter the third side size: '))

# if firstSide==secondSide==thirdSide:
#     print('Equilateral triangle')
# elif firstSide==secondSide or secondSide==thirdSide or firstSide==thirdSide:
#     print('Isosceles triangle')
# else:
#     print('Diffrent sided triangle')

#There are 1,2,5 and 10 value coins. Use minimum number of coins for input cost-------------------------------
# from math import floor
# cost=int(input('Please enter a cost: '))
# print('We use')
# if cost>=10:
#     tenCoin=floor(cost/10)
#     cost=cost%10
#     print(tenCoin,' tenCoin,')
# if cost>=5:
#     fiveCoin=floor(cost/5)
#     cost=cost%5
#     print(fiveCoin, ' fiveCoin,')
# if cost>=2:
#     twoCoin=floor(cost/2)
#     print(twoCoin, ' twoCoin and ')
# if cost%2!=0:
#     print ('1 oneCoin')

#Finding maximum with/whitout math function-----------------------------------------------------------------
import math

#without math function
# a=[]
# max=-math.inf
# for i in range(5):
#     a.append(int(input("please enter a number: ")))
#     if a[i]>max:
#         max=a[i]
#         index=i
# print("in list:",a,"maximum is:",max,"and it is in",index+1,"place")

#with max function
# a=[]
# for i in range(5):
#     a.append(int(input("please enter a number: ")))
# max=max(a)
# print("in list:",a,"maximum is:",max)

#calculator function-------------------------------------------------------------------------------------------

# def calculator(a,b,operator):
#     match operator:
#         case "+":
#             print("a+b=",a+b)
#         case "-":
#             print("a-b=",a-b)
#         case "*":
#             print("a*b=",a*b)
#         case "/":
#             print("a/b=",a/b)
#         case _:
#             print("please enter valid numbers and operator")

# a=int(input("Please enter the first number:"))
# b=int(input("Please enter the second number:"))
# operator=input("Please enter the operator:")
# calculator(a,b,operator)