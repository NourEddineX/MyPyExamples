#!/usr/bin/python3
print("Welcome To Marks Calculator")

name = str(input("Enter Student Name:\n") )
math = float(input("Enter Math Marks:\n") )
sci = float(input("Enter Science Marks:\n") )
eng = float(input("Enter English Marks:\n") )

if eng>50 or sci>50 or math>50:
 print("Error : max=50")
 quit()
##################
total=math+sci+eng
per=total/150*100
if per>50:
 print("Congratulations",name,"passed! your percentage is ",per,"!")
else:
 print("Hard Luck,",name,"Failed, Try harder next time")
##################
 