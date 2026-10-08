question1=('''YOUR FIRST QUESTION ON THE COMPUTER SCREEN IS "FIND THE VALUE OF THE GIVEN EXPRESSION 45+37''')
question2=('''YOUR SECOND QUESTION ON THE COMPUTER SCREEN IS FIND THE VALUE OF THE GIVEN EXPRESSION 120-45''')
question3=('''YOUR THIRD QUESTION ON THE COMPUTER SCREEN IS FIND THE VALUE OF THE GIVEN EXPRESSION 12*6''')
question4=('''YOUR FOURTH QUESTION ON THE COMPUTER SCREEN IS FIND THE VALUE OF THE GIVEN EXPRESSION 250+150''')
question5=('''YOUR FIFTH QUESTION ON THE COMPUTER SCREEN Is FIND THE VALUE OF THE GIVEN EXPRESSION 85-29''')

list1questions=[question1,question2,question3,question4,question5]
list2options=[["a=72","b=82","c=85","d=77"],["a=75","b=85","c=65","d=70"],["a=62","b=82","c=72","d=74"],["a=300","b=350","c=450","d=400"],["a=56","b=66","c=54","d=64"]]
list3correctoptions=["b=82","a=75","c=72","d=400","a=56"]
totalrupees=0
for question,option,correctoption in zip(list1questions,list2options,list3correctoptions):
    print(question,option)
    answer=(input())
    if answer==correctoption:
        print ("YOUR ANSWER IS CORRECT YOU RECIEVE RUPEES 10000")
        totalrupees+=10000
    else:
        print("SORRY,YOUR ANSWER IS WRONG,YOU CAN TAKE THE AMOUNT WON TILL NOW HOME")
        
        break
print ("TOTAL AMOUNT WON BY YOU IS ",totalrupees)



