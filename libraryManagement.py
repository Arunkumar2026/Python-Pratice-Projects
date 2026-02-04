'''
this is  a library management program in this program we can register the user,
add books to the library, view users, view books, borrow books from other users, 
and return the books to that user.
'''

import os # importing os module
import json # importing json module

USER_FILE = 'libraryUsers.json' # importing library users in the USER_FILE variable
BOOK_FILE = 'libraryBooks.json' # importing library books in the BOOK_FILE variable

#this function is to load the data in json file
def load_json(file_name):
    if not os.path.exists(file_name): # checking if the file is present or not, if the file is not present then the condition will be true.
        return [] # if the file is not present then we are returning the empty list
    try: # if the file is present then we are trying different methods
        with open(file_name,'r') as f: # opening the file and reading the file with 'r' method and saving the file with alias name f
           return json.load(f)
    # to handle the errors we have to use excepts
    except json.JSONDecodeError:
        return []

#this function will save the data in the user file
def save_json(file_name,data):
    with open(file_name, 'w') as f: #opening the file in wrirte mode 'w'
        #this dump function will save the user data in the user file 
        #data is the user data, f is the file mode, indent is the staring spaces
        json.dump(data,f,indent=4) 


#this function will register the new user 
def register_user(users):
    name = input("Enter your name: ").strip()

    #we have to check weather the user is already exist in the user date if the user is already exist then we should not register again.
    #to check this we have to use the conditon operator
    if any(u['name'] == name for u in users): # this is the generator expression with any() method  
        print("User already registered.\n")
        return users
    #if the user is not existed in the data then we have to register the new user
    user = {'name':name, 'borrowed_books': []}
    users.append(user)

    #we have to save this data in the user file 
    save_json(USER_FILE,users) #this function will save the data in the user file

    #showing the success message to the user 
    print(f'user: {name} registered successfully.\n')
    return users

#this view users function will show the number of users in the database
def view_users(users):
    #first we have to check if the user data is empty or not for this we use if condition
    if not users: #not is the membership operatior
        print('No registered users\n') #if the conditon is true then this print will execute the message
        return 
    #below code will execute if the users file is not empty
    print('----- Registered Users ------')
    #we have to use for loop to extract the data from the users file
    for idx,user in enumerate(users,start=1):
        borrowed_title = [b['title'] for b in user['borrowed_books']]
        print(f'{idx}. {user["name"]} - Borrowed Books: {borrowed_title}')
    print()

#this function will add books to the library
def add_book(books):
    #this is title variable will take the title of the book from the user
    title = input("Enter book title: ")
    #this author variable will take the author of the book 
    author = input("Enter author name: ")

    #this try block will ask they user that how many book does he want to add to the library
    try:
        quantity =  int(input("Enter quantity of books: "))
    #if the valueError is raised then the except block will handle that error 
    except ValueError:
        print("invalid quantity. setting quantity = 1")
        quantity = 1
    #the details which we have taken we have to append it to books variable
    books.append({
        "title":title,
        "author":author,
        'quantity':quantity
    })
    #the appended details should be saved for that we have to call the save_json function
    save_json(BOOK_FILE,books)
    #showing the succes message
    print(f'Book: {title} by {author} added with quantity {quantity}\n')

#this function will show the library books
def view_books(books):
    #first we have to check if there is any book is there or not with if conditon
    if not books:
        print("No books in the library\n")
        return
    #if books are there then this will be execute
    print("----- Library Books ------")
    #to view the books we have to use the for loop
    for idx,book in enumerate(books,start=1):
        print(f'{idx}. {book["title"]} by {book["author"]} [Quantity:{book["quantity"]}]')
    print()

#this function will find if the user is present in the user data or not
def find_user(users,name):
    #we have to loop through the each item in the user for this we have to use for loop
    for user in users:
        #each given name should be check with the user data with if conditon
        if user["name"] == name:
            #if the given name is present in the user data then the user will be return 
            return user
    #if the given name is not matched with user data then the None will be return
    return 



#this fucntion will the users to borrow books eachother
def borrow_book(books, users):
    #first we have to check if he user is exist or not for that we have to use if condition
    if not users:
        print("No users registered.\n")
        return books, users
    #if the have user date then the below code will be execute
    #then we have to take the user name
    user_name = input("Enter your name: ")
    #we have to check if the given name is present in the user data or not
    user = find_user(users,user_name)
    #we have to check if the user is present or not
    if not user:
        print("User not found.\n")
        #we have to return the books and users
        return books, users 
    #we have to call the view books function to show the books to the user
    view_books(books)
    #next we have to check the if the book are present or not
    if not books:
        return books, users
    try:
        choice = int(input("Enter book number: ")) - 1
        if 0 <= choice < len(books):
            if books[choice]['quantity'] > 0:
                books[choice]['quantity'] -= 1


                user['borrowed_books'].append({
                    "title":books[choice]['title'],
                    "author":books[choice]['author']
                })

                save_json(BOOK_FILE,books)
                save_json(USER_FILE,users)

                print(f'You borrowed {books[choice]["title"]} successfully')
            else:
                print("Sorry, out of stock")

        else:
            print("Invalid book number")
    except ValueError:
        print("Please enter valid number")
    return books, users

#this is the main function
def main():
    users = load_json(USER_FILE) # calling the load_json function and the returned data is stored in users variable 
    books = load_json(BOOK_FILE) # calling the load_json function and the returned data is stored in books variable

    # creating a inifinity while loop
    while True:
        # this are the menu options shown to the user
        print("===== LibrarySys Menu =====")
        print("1. Register User")
        print("2. View Users")
        print("3. Add Book")
        print("4. View Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        #taking the user input of the given options and storing it in the choice variable
        choice = input("Choose an option: ")

        #checking the option selected by the user with the conditions
        #if any option is matched with any condition then the assigned function will be called.
        if choice == "1":
            users = register_user(users)
        elif choice == "2":
            users = view_users(users)
        elif choice == "3":
            books = add_book(books)
        elif choice == "4":
            books = view_books(books)
        elif choice == "5":
            books, users = borrow_book(books, users)
        elif choice == "6":
            return_book(books, users)
        elif choice == "7":
            print("Existing LibrarySys... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n") 


main()