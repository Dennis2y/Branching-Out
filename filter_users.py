import json  # This allows us to work with JSON files (like reading or writing data)


# This function opens the file and gets all the users from it
def get_all_users():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)  # Load JSON data into a Python list
            return users
    except FileNotFoundError:
        print("The file users.json was not found.")
        return []
    except json.JSONDecodeError:
        print("The file is not a valid JSON.")
        return []


# This function finds users by name
def find_users_by_name(users, name):
    name = name.lower()  # make it lowercase so it's easier to compare
    return [user for user in users if user["name"].lower() == name]


# This function finds users by age
def find_users_by_age(users, age):
    return [user for user in users if user["age"] == age]


# This function finds users by email
def find_users_by_email(users, email):
    email = email.lower()
    return [user for user in users if user["email"].lower() == email]


# This function prints out each user nicely
def show_users(users):
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")


# This is the main part that runs when you start the program
if __name__ == "__main__":
    # First, get all users from the file
    users = get_all_users()

    if not users:
        exit()  # If we can't read users, stop the program

    # Ask user how they want to search
    print("What do you want to search by? (name, age, or email)")
    choice = input("Enter your choice: ").strip().lower()

    # If the user chooses to search by name
    if choice == "name":
        name_input = input("Enter the name: ").strip()
        result = find_users_by_name(users, name_input)
        show_users(result)

    # If the user chooses to search by age
    elif choice == "age":
        age_input = input("Enter the age: ").strip()
        if age_input.isdigit():  # Check if input is a number
            result = find_users_by_age(users, int(age_input))
            show_users(result)
        else:
            print("Please enter a valid number for age.")

    # If the user chooses to search by email
    elif choice == "email":
        email_input = input("Enter the email: ").strip()
        result = find_users_by_email(users, email_input)
        show_users(result)

    # If the input is not one of the three options
    else:
        print("You can only search by name, age, or email.")
