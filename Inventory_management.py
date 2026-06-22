import datetime   # import datetime to record transaction time

inventory = {}                   # dictionary to store products
transactions = []              # list to store transaction history

def load_inventory():                     # function to load data from file
    try:
        with open("inventory.txt","r") as f:                  # open file in read mode
            for line in f:
                pid,name,cat,price,qty,reorder = line.strip().split(",")                  # split values by comma
                inventory[pid] = {                       # store product details in dictionary
                    "name":name,
                    "category":cat,
                    "price":float(price),
                    "qty":int(qty),
                    "reorder":int(reorder)
                }
    except FileNotFoundError:             # if file not found, start empty
        pass

def save_inventory():                                # function to save data to file
    with open("inventory.txt","w") as f:    # open file in write mode
        for pid,data in inventory.items():
            f.write(f"{pid},{data['name']},{data['category']},{data['price']},{data['qty']},{data['reorder']}\n")

def add_product():              # function to add new product
    pid = input("Product ID: ").strip().upper()          # enter product ID
    if pid in inventory:                                             # check if ID already exists
        print("ID already exists!")                                             # show error
        return
    name = input("Name: ")                              # enter product name
    cat = input("Category: ")                               # enter category
    price = float(input("Price: "))                                           # enter price
    qty = int(input("Quantity: "))                    # enter quantity
    reorder = int(input("Reorder Level: "))   # enter reorder level
    inventory[pid] = {"name":name,"category":cat,"price":price,"qty":qty,"reorder":reorder}   # save product

def stock_in():                                              # function to add stock
    pid = input("Product ID: ").strip().upper()
    if pid in inventory:                        # check if product exists
        qty = int(input("Add Quantity: "))                                  # enter quantity to add
        inventory[pid]["qty"] += qty                                            # update stock
        log_transaction(pid,"IN",qty)                            # log transaction
    else:
        print("Product not found!")   # show error

def stock_out():                                          # function to deduct stock
    pid = input("Product ID: ").strip().upper()
    if pid in inventory:                                    # check if product exists
        qty = int(input("Deduct Quantity: "))            # enter quantity to deduct
        if qty <= inventory[pid]["qty"]:        # check if enough stock
            inventory[pid]["qty"] -= qty                # update stock
            log_transaction(pid,"OUT",qty)          # log transaction
        else:
            print("Insufficient stock!")             # show error
    else:
        print("Product not found!")              # show error

def view_inventory():                # function to view all products
    print("ID | Name | Category | Price | Qty | Value")                  # table header
    for pid,data in inventory.items():
        val = data["price"] * data["qty"]   # calculate value
        print(f"{pid} | {data['name']} | {data['category']} | {data['price']} | {data['qty']} | {val}")

def low_stock_alert():                      # function to show low stock items
    for pid,data in inventory.items():
        if data["qty"] <= data["reorder"]:              #check reorder level
            print(f"{pid} - {data['name']} low stock ({data['qty']})")

def generate_report():                         # function to generate summary report
    total_val = sum(d["price"]*d["qty"] for d in inventory.values())                 # total value
    cats = {d["category"] for d in inventory.values()}                # unique categories
    print(f"Total Products: {len(inventory)}")                # total products
    print(f"Total Value: Rs.{total_val}")            # total value
    print(f"Categories: {', '.join(cats)}")          # categories list

def log_transaction(pid,typ,qty):                                            # function to log transaction
    transactions.append((pid,typ,qty,datetime.datetime.now()))                           # add entry with timestamp
    # main program starts here
load_inventory()                             # load data at startup
while True:
    print("\n1.Add 2.Stock-In 3.Stock-Out 4.View 5.Alert 6.Report 7.Exit")                          # menu options
    ch = input("Choice: ")                          # enter choice
    if ch=="1": add_product()
    elif ch=="2": stock_in()
    elif ch=="3": stock_out()
    elif ch=="4": view_inventory()
    elif ch=="5": low_stock_alert()
    elif ch=="6": generate_report()
    elif ch=="7":
        save_inventory()   # save data before exit
        break
