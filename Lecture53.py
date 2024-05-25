#-------------------------------------------------------
def vatCalculate():
    price  = int(input("Please enter total Price:  "))
    result = price + (price * 7/100)
    return result

print("Net Price","=",vatCalculate(),"THB")   
#-------------------------------------------------------
