grades=["A+","A","B+","B","C+","C","D","F"]
correspondingpoints=[10, 9, 8, 7, 6, 5, 4, 0]
subjectnanmelist=[]
credits_list=[]
listofoptions=["ENTER MORE SUBJECTS AND CREDITS","EXIT"]
newlistofpointsscoring=[]
while True:
    print(listofoptions)
    userinput=int(input("SELECT FROM ONE OF THE OPTIONS FROM ABOVE WHETHER YOU WANT TO CONTINUE ENTERING SUBJECTS AND CORRESPONDING CREDITS BY CHOOSING 1 OR 2"))
    if userinput==1:
        subjectname=input("ENTER THE SUBJECT NAME THAT IS THE PART OF YOUR SYLLABUS")
        credits=int(input("ENTER THE NUMBE OF CREDITS ASSIGNED TO YOU IN THIS SUBJECT BY PROF"))
        subjectnanmelist.append(subjectname)
        credits_list.append(credits)
        userinput2=input("ENTER THE GRADES YOU ARE EXPECTING IN THAT COURSE")
        if userinput2!="A+" or userinput2!="A" or userinput2!="B+" or userinput2!="B" or userinput2!="C+" or userinput2!="C" or userinput2!="D" or userinput2!="F" :
            print("THIS GRADE DOES NOT EXIST ")
            
        if userinput2=="A+" or userinput2=="A" or userinput2=="B+" or userinput2=="B" or userinput2=="C+" or userinput2=="C" or userinput2=="D" or userinput2=="F"  :
     
            index= grades.index(userinput2)
            print("CORRESPONDING POINTS IN THAT SUBJECT YOU ARE SCORING IS EQUAL TO",correspondingpoints[index])
            newlistofpointsscoring.append(correspondingpoints[index])
            newlist=[x*y for x,y in zip(credits_list,newlistofpointsscoring)]

        








    if userinput==2:
        break
print("YOUR EXPECTGED CPI IS EQUAL TO",sum(newlist)/sum(credits_list))