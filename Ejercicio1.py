Library = {}
serial = len(Library)

print("====================================")
print("Welcome to your library database!")

menu = True
while menu:
    print("====================================")
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
            Library.update({serial:book})
            reset = input("Would you like to add another book? Y/N > ")
            if reset.upper() == "N":
                print(Library)
                initiate = False

    if option == "2":
        print("====================================")
        option2 = input("Press (1) to see all books or press (2) to search for a book: ")
        if option2 == "1":
            for key, item in Library.items():
                print(f"ID: {key} -------------------- Book: {item}")
        elif option2 == "2":
            booksearch = int(input("Enter the ID of the book you would like to see: "))
            print(Library.get(booksearch, "This item is not in our library."))

    if option == "3":
        print("====================================")
        for key, item in Library.items():
                print(f"ID: {key} -------------------- Book: {item}")
        u_book = int(input("Enter the ID of the book you would like to edit: "))
        u_title = input("Enter the title of the book: ")
        u_author = input("Enter the author of the book: ")
        u_year = input("Enter the release year of the book: ")
        updatedBook = {"title":u_title, "author":u_author, "year":u_year}
        Library[u_book] = updatedBook

    if option == "4":
        print("====================================")
        for key, item in Library.items():
                print(f"ID: {key} -------------------- Book: {item}")
        delete = int(input("Enter the ID of the book you would like to delete: "))
        Library.pop(delete)
        print("Item deleted successfully!")

    if option == "5":
        print("====================================")
        print("Thanks, come back later")
        menu = False
