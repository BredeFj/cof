#dictonaries used stores the coffe types and price same with sice and price
menu = {"Espresso": 2.50, "Americano": 3.00, "Latte": 2.50, "Mocha": 3.50, "Cappuccino": 3.00, "Flat White": 2.50, "Macchiato": 2.50}
sizes = {"medium": 0.00, "large": 1.00, "xl": 1.50 }



#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees.:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White.")
print(".----------------------------.")

price = 0
total_cups = 0

# asks the user how many cups they want to order then saves it in the variable total_cups 

total_cups = int(input("How many cups do you want to order? "))

#this loop will ask the user to input a valid amount of types of coffee based on how many they selected in the previous step it also implements fail checking where if the user inputs an invalid type of coffee it will tell them its not available and the ask them to try again
# it also keeps going until they enter a valid coffee type for each cup
order = []
for cup_number in range(total_cups):
   while True:
         coffee = input("What type of coffee would you like? ").title()
         if coffee in menu:
              price += menu[coffee]
              order.append(coffee)
              break
         else:
              print("sorry this type is not available")
             

# same as previous loop will ask the user to input a size based on how many cups they ordered and ask them to input a size for each type of coffee so if the order a flat white and latte it will ask them what sice flat white and what size latte making it easier for the user
for cup_number in range(total_cups):    
 coffee_choice = order[cup_number]
 while True:
         size = input("what size " + coffee_choice  + " medium large or xl " )
         if size in sizes:
                  price += sizes[size]
                  break
         else:
              print("sorry this is not available. try again")
     


# asks user if they want the coffee to go or not and saves it in location
location = input("Do you want it to go? yes/no ")


# if they want it to go it takes the total amount of cups and * it by 1 to get the fee for each cup if they and if they say no it doesnt add anything 
if location == "yes":
     total_takeaway = 1.00 * total_cups
     price += total_takeaway
elif location == "no":
   total_takeaway = 0




# prints the finals price of their order
print("----------------------------")
print("Total Cost: £" + str(price))
