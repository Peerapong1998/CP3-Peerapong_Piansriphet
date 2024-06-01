SystemMenu = {'ข้าวมันไก่':50,"เป็ดทอดเกลือ":60,"ข้าวไข่เจียว":50,"ต้มยำกุ้ง":80}
menuList = []

def  showBill():
     txtShop = "Welcome To Jabz Shop "
     print(txtShop.center(40,'*'))
     netPrice = 0
     for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        netPrice +=  int(menuList[number][1])
     print("Total Price","=",netPrice,"Bath")
     txtThank = "Thank You for support"
     print(txtThank.center(40,'*'))

#---------------------------------------------------
while True:
    menuName =  input("Please enter Menu:  ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,SystemMenu[menuName]])
print(menuList)
showBill()