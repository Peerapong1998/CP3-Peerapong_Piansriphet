menuList = []

def  showBill():
     shopName = "Yellow Shope"
     print(shopName.center(20,'*'))
     netPrice = 0
     for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        netPrice +=  menuList[number][1]
     print("Total Price","=",netPrice,"Bath")
     txtThank = "Thank you"
     print(txtThank.center(20,'*'))

#---------------------------------------------------
while True:
    menuName =  input("Please enter Menu:  ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice =  int(input("Please enter Price:  "))
        menuList.append([menuName,menuPrice])

showBill()