print ("This programme is to show exact time of order delievery: ")
order=int(input("What do you want to order: \n1.Laptops\n2.Mobiles\n3.Furnitures\n4.Utensils"))
rate=int(input("What is your Budget: \n1.Above 30000\n2.Above 20000\n3.Above 15000\n4.10000 - 15000\n5.8000 - 10000\n6.5000 - 8000\n7.Below 5000"))
if (order == 1 and rate ==1):
    placed=int(input("Place Your order Among: 1.DELL\n2.HP\n3.MSI\n4.Predator"))
