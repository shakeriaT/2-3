# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# itemName = "TV Stand"
# retailPrice = 325.00
# wholesalePrice = 200.00
# profit = 125.0
# Sale_Price = 243.75
# Sale_Profit = 43.75
Sale_Price = 243.75
Sale_Profit = 43.75
profit = 125.0

profit = retailPrice - wholesalePrice
Sale_Price = retailPrice - (retailPrice * 0.25)
Sale_Profit = Sale_Price - wholesalePrice


print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(Sale_Price))
print("Sale Profit: $" + str(Sale_Profit))