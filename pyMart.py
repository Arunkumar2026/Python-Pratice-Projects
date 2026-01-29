'''
This is Swiggy Clone Program 
which will show items to order we can add to cart, 
we can remove from cart, view the cart and checkout.
'''

#Welcome to swiggy clone program 

#This is the products which will be shown to the customer
products = { 
    1: {"name": "Apples", "price": 50},
    2: {"name": "Bananas", "price": 30},
    3: {"name": "Milk", "price": 60},
    4: {"name": "Bread", "price": 40},
    5: {"name": "Eggs (dozen)", "price": 70}
}

cart = {} #This is the cart which products are added to it.

#This function will show the products
def show_products():
    pass



#This is the menu which shows the products to the customers.
def menu(): 
    while True: #This is always True because it will run in inifity.
        #This is the navigation menu shown to the customer
        print("\n***** PyMart - Mini Shopping Cart *****")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        #Taking the input from the user
        choice = input("Enter your Choice: ").strip()
        #This are the conditions which will check the required choice from the customer
        if choice == "1": #This will be True if the choice is 1
            show_products() #Calling the function
        elif choice == "2": #This will be True if the choice is 2
            add_to_cart() #Calling the function
        elif choice == "3": #This will be True if the choice is 3
            remove_from_cart() #Calling the function
        elif choice == "4": #This will be True if the choice is 4
            view_cart() #Calling the function
        elif choice == "5": #This will be True if the choice is 5
            checkout() #Calling the function
        elif choice == "6": #This will be True if the choice is 6
            print("Exiting PyMart, GoodBye!")
            break #Breaking from the infinity while loop
        else: #If any of the conditions are not True then the else block will be exicute
            print("Invaild choice! Please try again.")


