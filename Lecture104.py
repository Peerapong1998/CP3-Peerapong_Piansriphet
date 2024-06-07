class Customer:
    name = "" 
    lastnmae = ""
    age = 0 
    def addCartz(self):
        print("Added to ",self.name,self.lastnmae,self.age,"s cart")

customer1 = Customer()
customer1.name = "Peerapong"
customer1.lastnmae = 'Piansriphet'
customer1.age = 25
customer1.addCartz()        

customer2 = Customer()
customer2.name = 'Thaitan'
customer2.lastnmae ='Ardvichat'
customer2.age = 24
customer2.addCartz()

customer3 = Customer()
customer3.name = 'Panya'
customer3.lastnmae = 'Saechai'
customer3.age = 23
customer3.addCartz()

customer4 = Customer()
customer4.name = 'Jiraphat'
customer4.lastnmae = 'Techapitakul'
customer4.age = 25
customer4.addCartz()