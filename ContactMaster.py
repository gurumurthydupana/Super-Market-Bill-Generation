# ContactMaster - Simple Contact Management Application

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"✅ Contact '{name}' added.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"✅ Contact '{name}' deleted.\n")
    else:
        print("Sorry ❌ Contact not found.\n")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"📞 {name}: {contacts[name]}\n")
    else:
        print("sorry ❌ Contact not found.\n")

def show_all_contacts():
    if contacts:
        print("\n📋 Contact List:")
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")
        print()
    else:
        print("Your Contact list is empty.\n")

def main():
    while True:
        print("ContactMaster Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Please Enter your option (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            show_all_contacts()
        elif choice == '5':
            print("End ContactMaster. Goodbye!")
            break
        else:
            print("❌ Please choose valid option. Please try again.\n")

if __name__ == "__main__":
    main()
