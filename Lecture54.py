def Login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else :
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("------------------")

def menuSelect():
    userSelected = int(input("Please select Choice Menu :  "))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print(result)
    
def PriceCalculate2():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

#user login


if Login()== True:
    showMenu()
    userselected = menuSelect()
    if userselected == 1:
        netPrice =  int(input("Please Enter Product Prcie:  "))
        print("Net Price","=",vatCalculate(netPrice),"Baht")
    elif userselected == 2:
        print("Total Price","=",PriceCalculate2(),"Baht")
    else:
        print("Don't have select")
print("*****************Thank You*****************")