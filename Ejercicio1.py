Library = {}
Books = {}
serial = len(Library)

print("====================================")
print("Welcome to your library database!")

menu = True
while menu:
    print("What would you like to do?: ")
    print("====================================")
    print("1. Add a new book")
    print("2. See all books/Search for a book")
    print("3. Update a book")
    print("4. Delete a book")
    print("5. Exit")
    while True: 
        option = input("Select an option: 1/2/3/4/5: ")
        if option.isdigit():
            break
        else:
            print("Please enter a valid option")
    if option == "1":
        initiate = True
        while initiate:
            serial += 1
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the release year of the book: ")
            book = {"title":title, "author":author, "year":year}
            Books.update({serial:book})
            Library.update(Books)
            reset = input("Would you like to add another book? Y/N > ")
            if reset.upper() == "N":
                print(Books)
                print(Library)
                initiate = False
            