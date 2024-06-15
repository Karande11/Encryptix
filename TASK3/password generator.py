#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    while True:
        print("\n===== Password Generator =====")
        print("1. Generate Password")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            length = int(input("Enter the password length (at least 8 characters): "))
            password = generate_password(length)
            if password:
                print("Generated Password: ", password)
        elif choice == '2':
            print("Exiting the password generator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




