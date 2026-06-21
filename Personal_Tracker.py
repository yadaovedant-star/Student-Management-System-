# Personal expense tracker
# Helps the user manage spending and stay within budget.


expense_records = []     # Stores all expenses entered by the user.


monthly_budget_limit = 0.0        # Keeps the monthly budget limit.



def validate_amount(amount_text):           # Checks if the amount entered is valid.
    try:
        amount_value = float(amount_text)
        if amount_value <= 0:
            raise ValueError                 #gives error
        return amount_value
    except ValueError:
        print("Please enter a positive number.")           # tells to give positive number if error occurs
        return None


# Adds one expense to the list.
def add_expense():
    expense_description = input("Enter expense description: ").strip() # Asking input to express whats the expense about for ex food,travel
    expense_category = input(
        "Enter category (Food/Travel/Bills/Entertainment/Other): "
    ).strip()

    expense_amount = None
    while expense_amount is None:                                                  #if none expense amount
        expense_amount = validate_amount(input("Enter amount: "))                      #asks again to input 

    expense_date = input("Enter date (DD-MM-YYYY): ").strip()          #date of expense
 
    expense_records.append(
        {
            "description": expense_description,                 #APPENDS ANDS ADDS THE DATA JUST ENTERED 
            "category": expense_category,      #CATEGORY
            "amount": expense_amount,       #AMOUNT
            "date": expense_date,      #DATE
        }
    )
    print("Expense added successfully!")       #SUCCESS


# Shows every expense in a clean format.
def show_all_expenses():                                
    if not expense_records:
        print("No expenses recorded yet.")                  #EXECUTES WHEN NO EXPENSE IS RECORDED 
        return

    print("\n=== All Expenses ===")
    for index, expense in enumerate(expense_records, start=1):                    #All expenses
        print(
            f"{index}. {expense['description']} | "
            f"{expense['category']} | Rs.{expense['amount']:.2f} | "
            f"{expense['date']}"
        )


# Shows how much was spent in each category.
def show_category_summary():                             #Shows full summary
    if not expense_records:
        print("No expenses recorded yet.")
        return

    category_total = {}
    for expense in expense_records:
        category = expense["category"]              #shows all categories with amount 
        category_total[category] = category_total.get(category, 0) + expense["amount"]

    print("\n=== Category Summary ===")
    for category, total_amount in category_total.items():     #total amount and items
        print(f"{category}: Rs.{total_amount:.2f}")


# Finds the category with the highest spending.
def find_top_category():
    if not expense_records:         #records
        return None

    category_total = {}
    for expense in expense_records:
        category = expense["category"]
        category_total[category] = category_total.get(category, 0) + expense["amount"]

    return max(category_total, key=category_total.get)


# Shows budget details and warning messages.
def show_budget_report():
    global monthly_budget_limit             # Budget report monthly and limts

    if monthly_budget_limit <= 0:
        print("Budget is not set yet.")         #if no budget is set
        return

    total_spent = sum(expense["amount"] for expense in expense_records)                #total expense formulae
    remaining_amount = monthly_budget_limit - total_spent                              #remaining left money 
    used_percentage = (total_spent / monthly_budget_limit) * 100                       # % expense 

    print("\n========= Budget Report =========")             #report                    
    print(f"Total spent   : Rs.{total_spent:.2f}")          #spent
    print(f"Budget limit  : Rs.{monthly_budget_limit:.2f}")       #budget
    print(f"Remaining     : Rs.{remaining_amount:.2f}")   #remains
    print(f"Used          : {used_percentage:.2f}%")   #used or remaining percent

    if used_percentage >= 100:
        print("ALERT: You have used your full budget.")           # if fully used prints ALERT: You have used your full budget.
    elif used_percentage >= 80:
        print("WARNING: You have already used more than 80% of your budget.")          #gives warning

    top_category = find_top_category()
    if top_category:
        print(f"Top category  : {top_category}")        # your top category for purchase
 

# Main menu of the program.
def main_menu():
    global monthly_budget_limit          

    while True:
        try:
            monthly_budget_limit = float(input("Set your monthly budget: "))         #monthly budget set
            if monthly_budget_limit <= 0:                #less than 0 or negative
                print("Budget must be a positive number.")     #prints this
                continue
            break
        except ValueError:
            print("Please enter a valid number for the budget.")          #error says to enter AGAIN 

    while True:
        print("\n------ Personal Expense Tracker ------")
        print("1. Add Expense")                                    #add your expense add()
        print("2. View All Expenses")         #views your expense
        print("3. Category Summary")     #category for your expense
        print("4. Budget Report")   #your report 
        print("5. Exit")      #exit the program

        choice = input("Enter your choice: ")           #choice selection

        if choice == "1":
            add_expense()          # adds expense
        elif choice == "2":
            show_all_expenses()     #views expense
        elif choice == "3":
            show_category_summary()    #shows category summary
        elif choice == "4":
            show_budget_report()     #shows budget report
        elif choice == "5":
            print("Exiting the expense tracker. Goodbye!")       #prints this msg while exiting
            break
        else:
            print("Invalid choice. Please try again.")       #else this


# Runs the program when the file is opened directly.
if __name__ == "__main__":
    main_menu()
