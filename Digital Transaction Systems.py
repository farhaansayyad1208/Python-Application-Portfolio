
history=[]
menu=["1.DEPOSIT","2.WITHDRAWAL","3.STATEMENT,4.EXIT","5.CHECK BALANCE"]
deposit=0
withdrawn=0
balance=1000



while True:
    print("SELECT FROM ONE OF THE OPTIONS IN THE",menu)
    userinput=(input())
    if userinput=="1.DEPOSIT" :
        deposittext=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT IN RUPEES"))
        balance+=deposittext
        history.append(f"YOUR LAST TRANSACTION WAS  DEPOSIT OF + { deposittext}")
        
    if  userinput=="2.WITHDRAWAL":
        withdrawaltext=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW IN RUPEES"))
        balance-=withdrawaltext
        if withdrawaltext<balance:
            history.append(f"YOUR LAST TRANSACTION WAS  WITHDRAWAL OF + { withdrawaltext}")
        
        if withdrawaltext>balance:
            print("YOU DO NOT HAVE SUFFICIENT AMOUNT IN YOUR ACCOUNT")
            print("YOUR CURRENT BALANCE IS ",balance+withdrawaltext)
    if userinput=="3.STATEMENT":
       if len(history)>5:
          print("YOUR STATEMENT IS:",history[-5:])
       else:
          print("YOUR STATEMENT IS:",history)
    if userinput=="5.CHECK BALANCE":
        print("YOUR CURRENT BALANCE IS ",balance)
    if userinput=="4.EXIT":
        
        break
print("THANK YOUR FOR VISITING,PLEASE VISIT AGAIN")
