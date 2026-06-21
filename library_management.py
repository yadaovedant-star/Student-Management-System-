import datetime

# This is the main storage for all books.
# Think of it like a small notebook where each book is saved using its ISBN.
book_catalog = {}


# This function adds a new book to the library.
# It asks for the ISBN, title, and author, then saves the book in the dictionary.
def add_book():
    # Ask the user for the book's unique ISBN.
    book_isbn = input("Enter ISBN: ").strip()

    # If the same ISBN already exists, don't add it again.
    if book_isbn in book_catalog:
        print("A book with this ISBN already exists.")
        return

    # Get the basic details of the book.
    book_title = input("Enter book title: ").strip()
    book_author = input("Enter author name: ").strip()

    # Save all details inside the catalog.
    # is_available tells us whether the book is currently free to borrow.
    # borrower_name and issue_date are empty until the book is issued.
    book_catalog[book_isbn] = {
        "title": book_title,
        "author": book_author,
        "is_available": True,
        "borrower_name": None,
        "issue_date": None,
    }
    print("Book added successfully!")


# This function lets a student borrow a book.
# It checks if the book exists and is not already issued.
def issue_book():
    # Ask for the ISBN of the book the user wants to issue.
    book_isbn = input("Enter ISBN: ").strip()

    # If the book is not in the catalog, it cannot be issued.
    if book_isbn not in book_catalog:
        print("Book not found.")
        return

    # If the book is already borrowed, we should not issue it again.
    if not book_catalog[book_isbn]["is_available"]:
        print("This book is already issued.")
        return

    # Take borrower details.
    borrower_name = input("Enter borrower name: ").strip()
    student_id = input("Enter student ID: ").strip()

    # Mark the book as issued.
    book_catalog[book_isbn]["is_available"] = False
    book_catalog[book_isbn]["borrower_name"] = f"{borrower_name} ({student_id})"
    book_catalog[book_isbn]["issue_date"] = datetime.date.today()

    # A book is due 7 days from the issue date.
    due_date = book_catalog[book_isbn]["issue_date"] + datetime.timedelta(days=7)
    print("Book issued successfully!")
    print(f"Title: {book_catalog[book_isbn]['title']}")
    print(f"Due date: {due_date}")


# This function handles returning a borrowed book.
# It updates the status and checks whether a fine is needed.
def return_book():
    # Ask which book is being returned.
    book_isbn = input("Enter ISBN: ").strip()

    # Make sure the book exists.
    if book_isbn not in book_catalog:
        print("Book not found.")
        return

    # If the book is already available, it means it was never issued.
    if book_catalog[book_isbn]["is_available"]:
        print("This book is not currently issued.")
        return

    # Calculate the due date using the stored issue date.
    issue_date = book_catalog[book_isbn]["issue_date"]
    due_date = issue_date + datetime.timedelta(days=7)
    today = datetime.date.today()

    # If the book is returned late, charge a small fine.
    overdue_fine = 0
    if today > due_date:
        days_overdue = (today - due_date).days
        overdue_fine = days_overdue * 2

    # Reset the book details so it becomes available again.
    book_catalog[book_isbn]["is_available"] = True
    book_catalog[book_isbn]["borrower_name"] = None
    book_catalog[book_isbn]["issue_date"] = None

    print("Book returned successfully!")
    if overdue_fine > 0:
        print(f"Overdue fine: Rs.{overdue_fine}")


# This function searches for books by matching part of a title or author name.
def search_book():
    # Ask the user for a search word.
    search_keyword = input("Enter title or author keyword: ").strip().lower()
    books_found = False

    # Check every book in the catalog.
    for book_isbn, book_details in book_catalog.items():
        title = book_details["title"]
        author = book_details["author"]

        # If the keyword matches either title or author, show the book.
        if search_keyword in title.lower() or search_keyword in author.lower():
            status = "Available" if book_details["is_available"] else "Issued"
            print(
                f"ISBN: {book_isbn} | Title: {title} | Author: {author} | Status: {status}"
            )
            books_found = True

    # If nothing matches, tell the user clearly.
    if not books_found:
        print("No matching books found.")


# This function shows all books currently stored in the library.
def view_catalog():
    # If there are no books, let the user know.
    if not book_catalog:
        print("The catalog is empty.")
        return

    print("\n=== Library Catalog ===")

    # Loop through the catalog and print each book's information.
    for book_isbn, book_details in book_catalog.items():
        if book_details["is_available"]:
            status = "Available"
        else:
            status = f"Issued to {book_details['borrower_name']}"

        print(
            f"ISBN: {book_isbn} | Title: {book_details['title']} | "
            f"Author: {book_details['author']} | Status: {status}"
        )


# This is the main menu that keeps the program running.
# It shows choices and calls the correct function based on user input.
def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. View Catalog")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        # Decide what to do based on the user's selection.
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            view_catalog()
        elif choice == "6":
            print("Exiting the library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# This line makes sure the menu runs only when the file is executed directly.
if __name__ == "__main__":
    menu()
