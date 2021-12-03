print("WELCOME TO THE PIZZA HUB!!!!!!!!!!!")
size=input("What size pizza do you want to order? S or M or L.")
if(size == "S"):
    bill= 12
    print("The pizza price will be $12")
    pepparoni=input("Do you want Pepparoni? Y or N.")
    if(pepparoni == "Y"):
        bill += 2

        print(f"The pizza price will be ${bill}..")
    cheese=input("Do you want extra cheese? Y or N.")
    if(cheese == "Y"):
        bill += 1

        print(f"The pizza price will be ${bill}..")
elif(size == "M"):
    bill = 15
    print("The pizza price will be $15")
    pepparoni=input("Do you want Pepparoni? Y or N.")
    if(pepparoni == "Y"):
        bill += 3

        print(f"The pizza price will be ${bill}..")
    cheese=input("Do you want extra cheese? Y or N.")
    if(cheese == "Y"):
        bill += 1

        print(f"The pizza price will be ${bill}..")
else:
    bill = 18
    print("The pizza price will be $18")
    pepparoni=input("Do you want Pepparoni? Y or N.")
    if(pepparoni == "Y"):
        bill += 3

        print(f"The pizza price will be ${bill}..")
    cheese=input("Do you want extra cheese? Y or N.")
    if(cheese == "Y"):
        bill += 1

        print(f"The pizza price will be ${bill}..")
