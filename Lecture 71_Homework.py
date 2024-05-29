menuList = []
priceList= []

def  showBill():
     totalPrice = 0
     print('----My food----')
     for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice +=  int(priceList[number])
     print("Net Price","=",totalPrice,"Bath")
#---------------------------------------------------
while True:
    menuName =  input("Please enter Menu:  ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice =  int(input("Please enter Price:  "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()