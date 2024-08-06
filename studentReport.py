""" 
INPUTS:
- name
- english
- maths
- science
- history
"""
name = input("Enter Name: ")

english = float(input("Enter English Score: ")) # 95
maths = float(input("Enter math score: ")) # 76
science = float(input("Enter science score: ")) # 60
history = float(input("Enter history score: ")) # 89

average_score = (english + maths + science + history) / 4

""" 
if subject score:
 >= 90 ---> excellent
 >= 75 ---> good
 >= 65 ---> average
 < 65 ---> poor 
"""

if english >= 90:
    print("English: Excellent")

elif (english >= 75) and (english < 90):
    print("English: Good")

elif (english >= 65) and (english < 75):
    print("English: Average")
else:
    print("English: Poor")


if maths >= 90:
    print("maths: Excellent")

elif (maths >= 75) and (maths < 90):
    print("maths: Good")

elif (maths >= 65) and (maths < 75):
    print("maths: Average")
else:
    print("maths: Poor")