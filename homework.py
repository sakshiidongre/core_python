# -*- coding: utf-8 -*-
"""homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ehpe6BpYZVKsFPjSrZQIzDq988Sqs_V7
"""

for i in range(10):
  a =i-1
  b= a+i
  print('interation and its addition:',b)

user=input("enter a string:")
print('original string:',user)

x=list(user)
for i in x[0:4:2]:
  print(i)

numbers_x = [10, 20, 30, 40, 100]
if numbers_x[0] == numbers_x[-1]:
  print("true")
else:
  print("false")

numbers=list( [10, 20, 33, 46, 55])
for i in numbers :
  if i %5 == 0:
    print(i," is divisible by 5")
  else:
    print(i,"is not divisible by 5")

str_x = "Emma is good developer. Emma is a writer"
cnt =str_x.count("iter")
print(cnt)

user =input("enter a string:")
user1 =input("enter a word whose count you wanna find from above string:")
cnt = user.count(user1)
print(user1,"has arrived",cnt,"tiimes in string")

n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="") 
    print()

for i in range(6):
  for j in range(1,i+1):
    print('*',end='')
  print()

for i in range(6):
  for j in range(i,-1):
    print(i,end='')
  print()

"""cumulative addition

"""

def cum():
  user = int(input("enter a number:"))
  add=0
  for i in range (1,user+1):
    add +=i
  print("total cumulative addition of ",user,"is",add)

cum()

names = ['swara','sahil','sanjana','khushi','kuku']
names.sort()
print(names)
names.extend([12,34])
print(names)

import random
number = random.randint(1,2)
user_num = int(input("enter a number:"))
print("checkingggg....")
if user_num==number :
  print("congratulation! you won the match")
else:
  print("sorry..better luck next time..it was {}".format(number))

import random
while (True):
  action = input("do you want to play the game?yes/no\n")
  if action == 'yes':
    number = random.randint(1,2)
    user_num = int(input("enter a number:"))
    points=0
    for i in range(3):
       if user_num == number :
          points+=4
          print("congratulation..you won the match..your points are {} ".format(points))
       else:
          print("sorry")
  if action=='no':
    exit

import random
point =0
while (True):
  action = input("do you want to play the game?yes/no\n")
  if action == 'yes':
    number = random.randint(1,3)
    user_num = int(input("enter a number:"))
    if user_num ==number :
        point +=4
        print("won...your score is {} ".format(point))
    else:
        print("sorry..try again")

  if action=='no':
    break

point = 0
point +=4
print(point)
for i in range(3):
  point+=4
  print(point)

import random
score=0
while 1:
  cgn=random.randint(1,9)
  for attempt in range(1,4):
    ugn = int(input("guess the num:"))
    if cgn == ugn:
      print("you won")
      if attempt ==1:
        score+=10
      elif attempt ==2 :
        score +=5
      elif attempt ==3:
        score+=1
      break
    elif cgn>ugn :
      print("your guess in high")
      print("no of attempts left :",3-attempt)
    elif cgn<ugn :
      print("your guess in low")
      print("no of attempts left :",3-attempt)

  ch = input("do you want to play again ?").lower().strip()
  if ch[0] == 'n':
    print("user chose the exit")
    print("your score is :",score)
    break

"""# **dictionary**"""

laptop ={'color':'silver','company':'hp','model':'15s','processor':'corei5','age':2,'windows':10,'storage':{'ssd':256,'hdd':256,'ram':8,'rom':4},
         'games':['GTA','SAN ANDREAS','TEMPLE RUN','patty']}
print(laptop)
laptop['color']='brown'
print(laptop)
print("ssd value is : ", laptop['storage']['ssd'])
print("total number of elements in games:",len(laptop['games']))



"""for loop over dict keys,values and items

"""

print(laptop.values())
print(laptop.keys())

for k,v in laptop.items():
  print(k,"------",v)

laptop.get('color')
laptop.update({'company':'acer','age':12})
laptop.pop('company')
laptop.popitem() #remove the last key
laptop.clear() #clear the dictionary

d1 ={0:123,1:45}
d1_copy= d1.copy()
d1.popitem()
print("d1 is :",d1)
print("d1 copy is :",d1_copy)

laptop.update({'company':'acer','age':12,'new':'swati','new2':'raman'})
laptop

"""# multiple login system1"""

db = {'neel':'123',
      'ratish':'r456',
      'shyam':'sh123'}
  
user=input("enter username:")
password = input("enter password:")

for user in db.keys():
     if password == db[user]:
        print("login sucessful")
        break
else :
    print("invalid password..please try with another password")

"""# multiple login system"""

db = {'neel':'123',
      'ratish':'r456',
      'shyam':'sh123'}

for attempts in range(1,4):
  username = input('Enter Username: ')
  Password = input('Enter Password: ')
  if username not in db.keys():
    print('access denied')
    print('No of attempts left: ',3- attempts)
  elif db[username] == Password:
    print('Login Successfull')
    break
  else:
    print('Wrong Creds!')
    print('No of attempts left: ',3- attempts)