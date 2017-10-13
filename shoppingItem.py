# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:42:31 2016
@author: maohuaxie
"""

class ShoppingItem:
    def __init__ (self, Name, Price, Qty):
        self.Name = Name
        self.Price = Price
        self.Qty = Qty
    def getName(self):
        return self.Name
    def getPrice(self):
        return self.Price
    def getItemTotalPrice(self):
        return self.Price*self.Qty
    def getQty(self):
        return self.Qty
    def setName(self, Name):
        self.Name = Name
    def setPrice(self, Price):
        self.Price = Price
    def setQty(self, Qty):
        self.Qty = Qty
    def __str__(self):
        state = getName() + "- $" + str(getPrice()) + " X " + str(getQty())
        return state
class Fruit(ShoppingItem):
    def __init__ (self, Name, Price, Qty, Origin):
        self.Name = Name
        self.Price = Price
        self.Qty = Qty
        self.Origin = Origin
    def setOrigin(self, Origin):
        self.Origin = Origin
    def getOrigin(self, Origin):
        return Origin
    def eat(self):
        print "I want to eat" + "\t" + getName()
class Meat(shoppingItem):
    def __init__ (self, Name, Price, Qty, Storage):
        self.Name = Name
        self.Price = Price
        self.Qty = Qty
        self.Storage = Stroage
    def setStorage(self, Strorage):
        self.Storage = Storage
    def getStorage(self, Storage):
        return Storage
    def cookMeat(self):
        print "I want to cook" + "\t" + getName()
    def crispMeat(self):
        print "I want to crisp" + "\t" + getName()
class Drink(shoppingItem):
    def __init__ (self, Name, Price, Qty, Storage):
        self.Name = Name
        self.Price = Price
        self.Qty = Qty
        self.Storage = Stroage
    def setStorage(self, Strorage):
        self.Storage = Storage
    def getStorage(self, Storage):
        return Storage
    def drink(self):
        print "I want to drink" + getName()
class Vgetable(shoppingItem): 
    def __init__ (self, Name, Price, Qty, Storage):
        self.Name = Name
        self.Price = Price
        self.Qty = Qty
        self.Storage = Stroage
    def setStorage(self, Strorage):
        self.Storage = Storage
    def getStorage(self, Storage):
        return Storage
    def Makesalad(self):
        print "I want to use" + getName() + "make salad"
        
class Customer:
    def __init__ (self, Name, Budget):
        self.Name = Name
        self.Budget = Budget
    def __str__(self):
        return "Customer name is " + Name 
    def getBudget(self):
        return self.Budget
    def setBudget(self):
        self.Budget = Budget
    def paycredit(self):
        print "credit"
    def paycash(self):
        print "cash"
        
    

name = input("what is your name? ")
print ("welcome  %s to your shopping list "% name)    
shoppinglist = []
while True:
    new_item = input("Please enter an item of your shopping list and type END when you have entered all of your items: ")
    if new_item == "END": 
        break
    shoppingList.append(new_item)
lengthe = len(shopppinglist)
print("Your shopping list is", length, "item long")
shoppinglist.sort
print(shoppinglist)




choice = 1
subtotal = 0 
price = 0        
discount = 0	        
print ("Steve's Groceries")
print ("\n")
print ("1.\tApples\t\t$%.2f per lbs" %1.99)
print ("2.\tOranges\t\t$%.2f per lbs" %2.19)
print ("3.\tChocolate Bar\t\t$%.2f earh"%0.99)
print ("4.\tIce Cream\t\t$%.2f a carton"%3.49)
print ("5.\tWatermelon\t\t$%.2f per lbs"%0.88)
print ("6.\tCottage Cheese\t\t$%.2f package"%1.29)
print ("7.\tMushrooms\t\t$%.2f per lbs"%1.59)
print ("8.\tNY Strip Steak\t\t$%.2f per lbs"%7.99)
print ("9.\tPizza\t\t$%.2f each"%4.99)
print ("10.\tStrawberries\t\t$%.2f each"%2.49)
print ("")
print ("0. Quit")
print ("");
print ("Your subtotal is $ " +str((int)(subtotal * 100) / 100.0))
print ("What would you like to purchase?  \nIf you have completed your checkout, enter 0.")


import random
choice = int( raw_input("Enter the number: "))
if choice == 0: 
    print "welcome back" 
elif choice == 1:
    price = 1.99
    print("How many do you want?")
    qty = int(raw_input("Enter the number: ")) 
elif choice == 2:
    price = 2.19
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))  
elif choice == 3:
    price = 0.99
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))
elif choice == 4:
    price = 3.49
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))        
elif choice == 5:
    price = 0.88
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))	
elif choice == 6:
    price = 1.29
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))
elif choice == 7:
    price = 1.59
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))	
elif choice == 8:
    price = 7.99
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))	
elif choice == 9:
    price = 4.99
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))	
elif choice == 10:
    price = 2.49
    print("How many do you want?")
    qty = int(raw_input("Enter the number: "))		         

subtotal = subtotal + (qty * price)	       
while choice > 0 :
    Input = raw_input("what you want pay: cash or credit")	         
    if  Input == "cash":
        discount = float( subtotal * .50*random.random())          
        tax = float((subtotal - discount) * 0.07);
        finalCost = subtotal - discount + tax;
        print("The subtotal is $%.2f " %(subtotal * 100) / 100.0)
        print("Paycash Discount $%.2f" %(discount * 100) / 100.0)
        print("Sales Tax $%.2f "% (tax* 100) / 100.0)
        print("Final price $%.2f"% (finalCost * 100) / 100.0)
def shoppinglist():
    quitshop = False
    shoppinglist = []
    while (quitshop==False):
        print(" ")
        print("You shopping list contains ")
        print(" ")
        for item in shoppinglist:
            print(item)
        print(" ")
        print("Menu")
        print(" ")
        print("0 = add multiple items to list")
        print("1 = add item to  list")
        print("2 = remove item from end")
        print("3= remove specific item")
        print("4 = reverse list")
        print("5 = print out some of the list")
        print("6 = sort into alphabetical order")
        print("9 = quit")
        userchoice = int(input("Please enter the option you want to proceed wiht "))
        if (userchoice == 0):
            print("you chose option 0")
            additem=""
            while additem != "stop":
                additem = input("Please enter item for list: ")
                if additem !="stop" and additem !="":
                    shoppinglist.append(additem)
        elif (userchoice ==1):
            print("You chose option 1")
            additem = input("please enter an item you want to add: ")
            shoppinglist.append(additem)
        elif (userchoice == 2):
            print ("You chose option 2")
            print("The program will reomve the last item from the list")
            shoppinglist.pop()
        elif (userchoice == 3):
            print("You chose option 3")
            positiontodel = int(input("Which item would you like to delete?))(enter a number)"))
            del(shoppinglist[positiontodel])
        elif (userchoice == 3):
            print("You chose option 4")
            print("This will reverse your list")
            shoppinglist.reverse()
        elif (userchoice == 5):
             print("You chose option 5")
             end = int (input("Which item should we end at? (insert a number)"))
             for printlist in range(end):
                 print (shoppinglist[printlist])
        elif (userchoice == 6):
            print ("You chose option 6")
            shoppinglist.sort()
        elif (userchoice == 9):
            print("You chose option 6")
            shoppinglist.sort()
        elif (userchoice == 9):
            print ("You have chosen to quit the program")
            quit
            quitshop = True
        else:
            print ("error")
            print("Try again")

    
