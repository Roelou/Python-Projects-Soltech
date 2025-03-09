import os  #Laai ie library op sodat die program kan werk op CMD


def add(a, b):      #Funksie vir plus somme
    return a + b

def subtract(a, b):     #Funksie vir minus somme
    return a - b

def multiply(a, b):     #Funksie vir maal somme
    return a * b

def divide(a, b):       #Funksie vir deel somme
    if b == 0:
        return "Error: Cannot divide by zero"       #Eception vir null dividing
    return a / b

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')        #Kode om vorige resultate te verwyder

def calculator():
    previous_result = None
    while True:
        print("\nSimple Calculator")        #Gee 'n menu vir die USER om die tipe wiskunde te kies wat hulle wil doen
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Clear Screen")
        print("6. Exit")
        
        choice = input("Enter your choice: ")       #Input vir die User se keuse
        
        if choice == '6':
            print("Exiting calculator...")      #Exit option
            break
        elif choice == '5':
            clear_screen()      #Verwyder vorige somme
            continue
        elif choice in ('1', '2', '3', '4'):
            try:
                if previous_result is not None:
                    use_previous = input("Do you want to use the previous result for a new equation? (yes/no): ").strip().lower()
                    if use_previous == 'yes':
                        num1 = previous_result      #Eerste input word ou antwoord
                    else:
                        num1 = float(input("Enter first number: "))         #Input vir die nommers wat gaan verwerk word
                else:
                    num1 = float(input("Enter first number: "))         #Input vir die nommers wat gaan verwerk word
                
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    previous_result = add(num1, num2)       #Roep en print funksies
                elif choice == '2':
                    previous_result = subtract(num1, num2)
                elif choice == '3':
                    previous_result = multiply(num1, num2)
                elif choice == '4':
                    previous_result = divide(num1, num2)

                print(f"Result: {previous_result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")        #Exception vir waardes wat nie kan annvaar word nie
        else:
            print("Invalid choice. Please select a valid option.")      #Exception vir keuse wat nie kan annvaar word nie

if __name__ == "__main__":
    calculator()        #Roep om die kode te begin
