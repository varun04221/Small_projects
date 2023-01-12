#Made By Varun kumar | Roll Number:2022563 | IIIT-DELHI

import requests
from random import randint

categories={1:"Arts and Literature",2:"Film and T.V.",3:"Food And Drink",4:"General Knowledge",5:"Geography",6:"History",7:"Music",8:"Science",9:"Society and Culture",10:"Sports and Leisure"}
print('''
WELCOME
Please Select A Category of your Interest to get satrted with the Quiz''')
for i in categories:
    print(i,categories[i])

sn=int(input("Enter The Serial Number of Selected Category:"))
nq=int(input("Please Enter the Number of questions you wish to Attempt:"))
print("""Difficulty
1. Easy
2. Medium
3. Tough""")
difficulty=int(input("Please Select the difficulty Level(Number Corresponding to it.):"))
if difficulty==1:
    difficulty="easy"
elif difficulty==2:
    difficulty='medium'
elif difficulty==3:
    difficulty='hard'
scat=categories[sn].replace(" ","_")
scat=scat.lower()
scat=scat.replace(".","")
rurl="https://the-trivia-api.com/api/questions?categories=%s&limit=%d&difficulty=%s"%(scat,nq,difficulty)


data=requests.get(rurl)
data=data.json()

totalcorrect=0
print('*'*50)
for i in data:
    question=i["question"]
    cao=randint(0,3)
    correct=i["correctAnswer"]
    Options=i["incorrectAnswers"]
    Options.insert(cao,correct)
    print(question)
    for i in range(len(Options)):
        print(i+1,Options[i])
    opt=int(input("Please Enter The No. Corresponding to selected Option:"))-1
    if opt==cao:
        print("Congratulations! You got it Right.")
        totalcorrect+=1
    else:
        print("Oops! that's Incorrect")
        print("Correct Answer is",correct)
    print('\n')
    print('*'*50)


print("Your Performance".center(40,'*'))
print(totalcorrect,'/',nq)
print(round((totalcorrect/nq)*100,2),'%')
