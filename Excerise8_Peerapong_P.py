# หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
usernameInput = input("Username : ")
passwoordInput = input("Password: ")

if usernameInput == 'admin' and passwoordInput == '1234':
    print("-----------------Welcome to Shop-------------------")
    print("------------------List menu-------------------------")
    print("---------------1.Notebook 25000(thb)")
    print("---------------2.Pc 30000 (thb)")
    print("---------------3.Macbook  50000(thb)")
    userSelected = int(input("Choose Product :   "))
    if userSelected == 1:
       print("1.Notebook:")
       unit = int(input("How much  :  "))
       priceProduct = 25000
       total = unit * priceProduct
       print("คุณต้องจ่ายเงินทั้งหมด :  ",total)
    elif userSelected == 2:
       print("2.Pc:")
       unit = int(input("How much :  "))
       priceProduct = 30000
       total = unit * priceProduct
       print("คุณต้องจ่ายเงินทั้งหมด :  ",total)

    elif userSelected == 3:
       print("3.Macbook:")
       unit = int(input("How much :  "))
       priceProduct = 50000
       total = unit * priceProduct
       print("คุณต้องจ่ายเงินทั้งหมด :  ",total)
       
print("------ขอบคุณที่ใช้บริการร้านเรานะ------------")