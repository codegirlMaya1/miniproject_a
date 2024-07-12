import os

old_path='add_contact.txt'
new_path=os.path.join('newdir','add_contact.txt') 
os.rename(old_path,new_path)

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_Newcontact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts[name] = contact
        print(f"{name} was added to your contact list.")
    

    def view_Yourcontacts(self):
        if self.contacts:
            for name, contact in self.contacts.items():
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print()
        else:
            print("Your contact list is empty.")

    def edit_Existingcontact(self, name, new_phone, new_email):
        if name in self.contacts:
            contact = self.contacts[name]
            contact.phone = new_phone
            contact.email = new_email
            print(f"{name}'s contact is now updated.")
        else:
            print(f"{name} is not listed in your current contacts.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} was removed from  your contacts.")
        else:
            print(f"{name} is not in your contacts currently.")

def main():
    contact_manager = ContactManager()

    while True:
        print("Contact Management Menu:")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("Please enter your # choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact_manager.add_Newcontact(name, phone, email)
        elif choice == "2":
            contact_manager.view_Yourcontacts()
        elif choice == "3":
            name = input("Enter the name of the contact to edit: ")
            new_phone = input("Enter the correct phone number: ")
            new_email = input("Enter the correct email address: ")
            contact_manager.edit_Existingcontact(name, new_phone, new_email)
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
            
        elif choice== "A":
            with open('add_contact.txt', 'w')as file:
                file.write(str(Contact))
                print(old_path)
        elif choice=="B":
            print(new_path)
        elif choice == "5":
            print("Now exiting the system....")
            break
        else:
            print("Invalid choice. Please make another selection.")
        try:
            ValueError
        except:
            ValueError
            print("please provide an accurate phone number, email and try again")

if __name__ == "__main__":
    main()