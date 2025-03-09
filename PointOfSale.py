import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')        #Kode om vorige resultate te verwyder


def display_products(products):     #Funksie om al die items te vertoon en di3 totaal the bereken
    if not products:
        print("No products in the list.")
        return
    
    total = 0
    print("\nProducts List:")
    print("---------------------------")
    for item, price in products:
        print(f"{item:<10} R{price:.2f}")
        total += price
    print("---------------------------")
    print(f"Total      R{total:.2f}")


def add_product(products):      #Funksie om items te laai op die POS systeem
    try:
        item = input("Enter product name: ")
        price = float(input("Enter product price: R"))
        products.append((item, price))
        print(f"{item} added successfully!")
    except ValueError:
        print("Invalid price. Please enter a numeric value.")


def pos_system():       #Main funksie om bewerkings te doen
    products = []       #Produk lys
    
    while True:
        print("\nPoint of Sale System")         #Gee opsies vir USER
        print("1. Add Product")
        print("2. Display Products")
        print("3. Clear Screen")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '4':
            print("Exiting POS system...")
            break
        elif choice == '3':         #Roep funksies om bewerkings te doen
            clear_screen()
        elif choice == '2':
            display_products(products)
        elif choice == '1':
            add_product(products)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    pos_system()
