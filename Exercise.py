Apple = 10
Banana = 20
Rice = 30

Usernameinput = input("Username :")
Passwordinput = input("Password :")
if Usernameinput == "User" and Passwordinput == "1234":
    print("---- Super market ----")
    print("1.Apple 10 bath")
    print("2.Banana 20 bath")
    print("3.Rice  30 bath")
    userSelected = int(input(">>"))
    if userSelected == 1:
        item = "Apple"
        number = int(input("Enter number of item :"))
        total = Apple*number
    elif userSelected == 2:
        item = "Banana"
        number = int(input("Enter number of item :"))
        total = Banana*number
    elif userSelected == 3:
        item = "Rice"
        number = int(input("Enter number of item :"))
        total = Rice*number
    else:
        print("Item not found")

    print(item,"---------------","x", number, "total =", total, "BTH")
else:
    print("Incorrect pls try again")    
