from datetime import date
import json

# this is the function to save the created application to a json file
def save_applications():
    with open("applications.json", "w") as file:
        json.dump(applications, file, indent=4)

# this is the function to load the json file
# if the file doesn't exist yet, the program will start with an empty list
def load_applications():
    try:
        with open("applications.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

applications = load_applications()

# this is the function to add applications
def add_application():
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status: ")
    date_applied = str(date.today())
    print("Date applied: " + date_applied)
    notes = input("Notes: ")

    # creates a dictionary that contains all the information about an application
    application = {
        "company": company,
        "role": role,
        "status": status,
        "date_applied": date_applied,
        "notes": notes,
    }

    applications.append(application)
    save_applications()
    print("Application added.\n")

# this is the function to view the applications of the user
def view_applications():
    if not applications:
        print("You have not added any applications.\n")
        return

    for index, application in enumerate(applications, start=1):
        print(f"Application #{index}")
        print(f"Company: {application['company']}")
        print(f"Position: {application['role']}")
        print(f"Status: {application['status']}")
        print(f"Date applied: {application['date_applied']}")
        print(f"Notes: {application['notes']}\n")

# main function where everything happens
def main():
    print("Welcome to the Application Tracker™!")

    while True:
        print("====================")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Exit")
        print("====================")

        choice = input("Enter your selection: ").strip()

        if choice == "1":
            print()
            add_application()

        elif choice == "2":
            print()
            view_applications()

        elif choice == "3":
            print("\nThank you for using Application Tracker!\n")
            break

        else:
            print("Invalid selection.\n")

main()