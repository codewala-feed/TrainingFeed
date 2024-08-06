""" 
INPUTS:
- name
- english
- maths
- science
- history
"""
name = input("Enter Name: ").upper()

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

print(f"{name} Report Card")
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


if science >= 90:
    print("science: Excellent")

elif (science >= 75) and (science < 90):
    print("science: Good")

elif (science >= 65) and (science < 75):
    print("science: Average")
else:
    print("science: Poor")


if history >= 90:
    print("history: Excellent")

elif (history >= 75) and (history < 90):
    print("history: Good")

elif (history >= 65) and (history < 75):
    print("history: Average")
else:
    print("history: Poor")
# --------------------------------------------------------------------
if average_score >= 90:
    overall_performance = "Excellent" 
    feedback = "Keep up the great work! You're excelling in all subjects."

elif (average_score >= 75) and (average_score < 90):
    overall_performance = "Good"  
    feedback = " You're doing well, but there's room for improvement in some areas."

