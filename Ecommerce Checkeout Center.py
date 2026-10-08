items = [] 
quantities = []

while True:
    userinput=(input('''SELECT FROM ONE OF THE OPTIONS "BUY MORE ITEMS" OR "EXIT"'''))
    if userinput=="BUY MORE ITEMS":
        userinput2=(input("WHICH ITEM DO YOU WANT TO BUY"))
        if userinput2 not in items:
        
            items.append(userinput2)
            quantities.append(1)
            
        for item in items:
                if item==userinput2:
                    i=items.index(userinput2)
                if items[i]==userinput2:
                    quantities[i]+=1
                
                
                    
                    







    if userinput=="EXIT":
        print("THANK YOU FOR VISITING OUR SHOP")
        break 
print (items)
print(quantities)