#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def main():
    while True:
        print("\n===== Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:



