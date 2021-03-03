# FEB 12
'''You are given a dictionary priceList = {"Pen": 10, "Pencil": 5, "Eraser": 5, "Ruler": 20}, representing products and their rates.

✔ Write a function rate that accepts this dictionary along with the name of a product and returns the price of that product. If the product
does not exist in the dictionary, then it should return -1. For example, if the name of the product is Ruler then the function should return 20

✔ Write another function update to modify the dictionary. The function should accept the dictionary, name of a product and new rate for it.
The function should return the updated dictionary as per the following cases - 

  Case 1: If the rate of the product is negative or zero and the product exists in the dictionary then the product should be removed from the dictionary

  Case 2: If the rate of the product is positive and the product exists in the dictionary then the rate of the product in the dictionary should be changed to the new rate that is passed to the function 

  Case 3: If the rate of the product is positive and the product does not exists in the dictionary then the product-rate pair should be added to the dictionary
'''

priceList = {
  "Pen": 10,
  "Pencil": 5,
  "Eraser": 5,
  "Ruler": 20
}

def rate(prices, product):
  if product in prices:
    return prices[product]
  
  return -1

def update(prices, product, newRate):
  if newRate <= 0 and product in prices:
    del prices[product]
  elif newRate > 0 and product in prices:
    prices[product] = newRate
  elif newRate > 0 and product not in prices:
    prices[product] = newRate
  
  return prices

print ("Rate of Pen: ", rate(priceList, "Pen"))
print ("Updated dictionary: ", update(priceList, "Pen", -1))
print ("Updated dictionary: ", update(priceList, "Pen", 15))
print ("Updated dictionary: ", update(priceList, "Sharpener", 5))