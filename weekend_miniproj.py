''' Your task is to develop a Contact Management System with the following features:
1. User Interface: The user should be able to interact with the program through a menu in the console.
2. Add a contact: The user should be able to add a new contact to the contact list. Each contact should have a name, phone number, and email address. (Use a dictionary to store the contact information)
3. Menu Actions: The user should be able to view all contacts, search for a contact by name, edit a contact, and delete a contact.
4. User Interaction: The user should be able to interact with the program until they choose to quit. Use regex to validate the phone number and email address.
5. Error Handling: The program should handle errors gracefully and allow the user to continue using the program after an error occurs.
6. Create an interactive readme file that explains how to use the program and its features.
7. Use functions to organize your code and make it more readable.
'''

import re
import os

#-----------------Global Variables----------------
contacts = {}



#-----------------Functions----------------

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def add_contact():
    while True:
        
        contact_first = input('Enter the contact first name: ')
        valid_firstname = re.match(r'[A-Z][a-z]+', contact_first) # Verify that the name is valid using a regex pattern and match()
        if valid_firstname:
            valfirst = contact_first
            print(f'You have added the first name: {contact_first}')
            break
        else:
            print('Invalid first name. Please enter a valid name.')
            continue
    while True:
        contact_last = input('Enter the contact last name: ')
        valid_lastname = re.match(r'[A-Z][a-z]+', contact_last) # Verify that the name is valid using a regex pattern and match()
        if valid_lastname:
            vallast = contact_last
            print(f'You have added the last name: {contact_last}')
            break
        else:
            print('Invalid last name. Please enter a valid name.')
            continue
    while True:
        contact_phone = input('Enter the contact phone number: ')
        valid_phone = re.match(r'^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$', contact_phone) # Verify that the phone number is valid using a regex pattern and match()
        if valid_phone:
            valphone = contact_phone
            print(f'You have added the phone number: {contact_phone}')
            break
        else:
            print('Invalid phone number. Please enter a valid phone number.')
            continue
    while True:
        contact_email = input('Enter the contact email address: ')
        valid_email = re.match(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', contact_email) # Verify that the email address is valid using a regex pattern and match()
        if valid_email:
            valemail = contact_email
            print(f'You have added the email address: {contact_email}')
            break
        else:
            print('Invalid email address. Please enter a valid email address.')
            continue
    contacts[valfirst] = {'First_Name': valfirst, 'Last_Name': vallast, 'Phone': valphone, 'Email': valemail}
    print(f'You have added the contact: {contacts[valfirst]}')   

def view_contacts():
    if len(contacts) == 0:
        print('You do not have any contacts in your contact list at this time.')
    else:
        print('Here are your contacts:')
        contact_list = list(contacts.items())
        for contact in contact_list:
            print(contact_list.index(contact) +1, end=' ')
            print(contact)
        


def edit_contact():
    view_contacts()
    try:
        contact_to_edit = int(input('Enter the contact you would like to edit: (select by number) '))
        contact_index = contact_to_edit - 1
        change_contact = list(contacts.values())[contact_index]
        print(change_contact)
        print(f'You have selected the contact: {contacts[change_contact]}')
        edit = int(input('What would you like to edit?\n1. First Name\n2. Last Name\n3. Phone Number\n4. Email Address\nEnter the number of your choice: '))
        while True:    
            try:
                if edit == 1:
                    new_firname = input('Enter the new contact first name: ')
                    valid_firstname = re.match(r'[A-Z][a-z]+', new_firname) # Verify that the name is valid using a regex pattern and match()
                    if valid_firstname:
                        contacts[change_contact]['First_Name'] = new_firname
                        print(f'You have edited the contact: {contacts[change_contact]}')
                        break
                    else:
                        print('Invalid first name. Please enter a valid name.')
                        continue
                while True:
                    if edit == 2:
                        new_lasname = input('Enter the new contact last name: ')
                        valid_lastname = re.match(r'[A-Z][a-z]+', new_lasname) # Verify that the name is valid using a regex pattern and match()
                        if valid_lastname:
                            contacts[change_contact]['Last_Name'] = new_lasname
                            print(f'You have edited the contact: {contacts[change_contact]}')
                            break
                        else:
                            print('Invalid last name. Please enter a valid name.')
                            continue
                while True:       
                    if edit == 3:
                        new_phon = input('Enter the new contact phone number: ')
                        valid_phone = re.match(r'^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$', new_phon) # Verify that the phone number is valid using a regex pattern and match
                        if valid_phone:
                            contacts[change_contact]['Phone'] = new_phon
                            print(f'You have edited the contact: {contacts[change_contact]}')
                            break
                        else:
                            print('Invalid phone number. Please enter a valid phone number.')
                            continue
                while True:            
                    if edit == 4:
                        new_emai = input('Enter the new contact email address: ')
                        valid_email = re.match(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', new_emai) # Verify that the email address is valid using a regex pattern and match
                        if valid_email:
                            contacts[change_contact]['Email'] = new_emai
                            print(f'You have edited the contact: {contacts[change_contact]}')
                            break
                        else:
                            print('Invalid email address. Please enter a valid email address.')
                            continue
                # while True: (Program freezes when I try to use this code block. I will need to troubleshoot this issue.)
                #     if edit == 5:
                #         custom_field = input('Enter the custom field you would like to add to the contact: ')
                #         [custom_value] = input(f'Enter the {custom_field}: ')
                #         contacts[custom_field] = custom_value
                #         print(f'You have added the custom field: {custom_field}, {custom_value} to the contact: {contacts[change_contact]}')
                #         break
                #     else:
                #         print('Please enter valid input.')
                #         continue
            except ValueError:
                print('Please enter a valid number.')
            except IndexError:
                print('Please enter a number within the available list parameters.')
            except KeyError:
                print('Please enter a valid number.')
    except ValueError:
        print('Please enter a valid number.')
    except IndexError:
        print('Please enter a number within the available list parameters.')

def delete_contact():
    view_contacts()
    try:
        contact_to_delete = int(input('Enter the contact you would like to delete: (select by number) '))
        delete_index = contact_to_delete - 1
        delete_contact = list(contacts.keys())[delete_index]
        del contacts[delete_contact]
        print(f'You have deleted the contact')
    except ValueError:
        print('Please enter a valid number.')
    except IndexError:
        print('Please enter a number within the available list parameters.')

def search_contact():
    search = int(input('''Enter the contact information you would like to search for: 
1. First Name
2. Last Name
3. Phone Number
4. Email Address
Enter the number of your choice: '''))
    if search == 1:
        nam_search = input('Enter the first name you would like to search for: ')
        name = nam_search.capitalize()
        first_list = list(contacts.keys())
        for line in first_list:
            if name in line:
                print(f'Contact found: {contacts[name]}')
            # else:
            #     print('Contact not found.')
        
    elif search == 2:
        lastsearch = input('Enter the last name you would like to search for: ')
        last_name = lastsearch.capitalize()
        for key, value in contacts.items():
            if last_name in value['Last_Name']:
                print(f'Contact found: {key}{value}')
            # else:
            #     print('Contact not found.')
    elif search == 3:
        phonesearch = input('Enter the phone number you would like to search for: ')
        for key, value in contacts.items():
            if phonesearch in value['Phone']:
                print(f'Contact found: {key}{value}')
            # else:
            #     print('Contact not found.')
    elif search == 4:
        emailsearch = input('Enter the email address you would like to search for: ')
        #valid_email = re.match(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', emailsearch)
        for key, value in contacts.items():
            if emailsearch in value['Email']:
                print(f'Contact found: {key}{value}')
            # else:
            #     print('Contact not found.')


# When searching, I am going to use the lambda function to sort the contacts by the key value of the dictionary. This will allow me to sort the contacts by name, phone number, or email address. I will also add a reverse alphabetical sort option. Resources: https://stackoverflow.com/questions/71637789/python-lambda-dictionary-sort

# def sort_contacts(): (This didnt work. It does something, but not what I expect it to. I will need to troubleshoot this issue.)
#     sort = int(input('How would you like to sort your contacts?\n1. Alphabetically\n2. By phone number\n3. By email address\n4. Reverse Alphabetically\n5. By Group\n6. By last name\n7. By last name reversed\nEnter the number of your choice: '))
#     contact = list(contacts.values())
#     try:
#         if sort == 1:
#             contact.sort(key=lambda x: x['First_Name'])
#             print('Your contacts have been sorted alphabetically.')
#             view_contacts()
#         elif sort == 2:
#             contact.sort(key=lambda x: x['Phone'])
#             print('Your contacts have been sorted by phone number.')
#             view_contacts()
#         elif sort == 3:
#             contact.sort(key=lambda x: x['Email'])
#             print('Your contacts have been sorted by email address.')
#             view_contacts()
#         elif sort == 4:
#             contact.sort(key=lambda x: x['First_Name'], reverse=True)
#             print('Your contacts have been sorted in reverse alphabetical order.')
#             view_contacts()
#         elif sort == 5:
#             contact.sort(key=lambda x: x['Group'])
#             print('Your contacts have been sorted by group.')
#             view_contacts()
#         elif sort == 6:
#             contact.sort(key=lambda x: x['Last_Name'])
#             print('Your contacts have been sorted by last name.')
#             view_contacts()
#         elif sort == 7:
#             contact.sort(key=lambda x: x['Last_Name'], reverse=True)
#             print('Your contacts have been sorted by last name in reverse order.')
#             view_contacts()
#     except ValueError:
#         print('Please enter a valid number.')
#     except IndexError:
#         print('Please enter a number within the available list parameters.')
    
def backup_contacts():
    
    with open('contacts.txt', 'w') as file:
        for key, value in contacts.items():
            file.write(str(f'{key}, {value}\n'))
        #file.write(str(contacts))
    print('Your contacts have been backed up to the contacts.txt file.')

# def restore_contacts(): # (This code block is not working. I will need to troubleshoot this issue.)
#     import_contacts = {}
#     with open('contacts.txt', 'r') as file:
#           lines = file.readlines() 
#           for line in lines:
#             key, value = line.strip().split(',')
#             import_contacts[key] = value
            
    # print('Your contacts have been imported from the .txt file.')
    # contacts.update(import_contacts)

def export_contacts():
    with open('exported_contacts.txt', 'w') as file:
        for contact, value in contacts.items():
            file.write(f'{contact}, {value}\n')
    print('Your contacts have been exported to the exported_contacts.txt file.')

def import_contacts(): 
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        import_contacts = {}
        for line in file:
            first_name, last_name, phone, email = line.strip().split(',')
            import_contacts[first_name] = {'First_Name': first_name, 'Last_Name': last_name, 'Phone': phone, 'Email': email}
            
        print('Your contacts have been imported from the .txt file.')
        contacts.update(import_contacts)
    
    

# def new_group(): # (This code block is not working. I will need to troubleshoot this issue.)
#     group = []
#     group_name = input('Enter the new group name (e.g., friends, family, work): ')
#     group.append(group_name)
#     contacts.append(group)
#     print(f'You have created the group: {group_name}')

# def view_groups():
#     if len(groups) == 0:
#         print('You do not have any groups in your contact list at this time.')
#     else:
#         print('Here are your groups:')
#         for group in groups:
#             print(groups.index(group) +1, end=' ')
#             print(group)

# def edit_group():
#     view_groups()
#     try:
#         group_to_edit = int(input('Enter the group you would like to edit: (select by number) '))
#         group_to_edit = group_to_edit - 1
#         group = groups[group_to_edit]
#         group['Name'] = input('Enter the new group name: ')
#         print(f'You have edited the group: {group}')
#     except ValueError:
#         print('Please enter a valid number.')
#     except IndexError:
#         print('Please enter a number within the available list parameters.')

# def delete_group():
#     view_groups()
#     try:
#         group_to_delete = int(input('Enter the group you would like to delete: (select by number) '))
#         group_to_delete = group_to_delete - 1
#         deleted_group = groups.pop(group_to_delete)
#         print(f'You have deleted the group: {deleted_group}')
#     except ValueError:
#         print('Please enter a valid number.')
#     except IndexError:
#         print('Please enter a number within the available list parameters.')

# def add_contact_to_group():
#     view_contacts()
#     view_groups()
#     try:
#         contact_to_add = int(input('Enter the contact you would like to add to a group: (select by number) '))
#         contact_to_add = contact_to_add - 1
#         contact = contacts[contact_to_add]
#         group_to_add = int(input('Enter the group you would like to add the contact to: (select by number) '))
#         group_to_add = group_to_add - 1
#         group = groups[group_to_add]
#         group.append(contact)
#         print(f'You have added the contact: {contact} to the group: {group}')
#     except ValueError:
#         print('Please enter a valid number.')
#     except IndexError:
#         print('Please enter a number within the available list parameters.')

# def remove_contact_from_group():
#     view_contacts()
#     try:
#         contact_to_remove = int(input('Enter the contact you would like to remove from the group: (select by number) '))
#         contact_to_remove = contact_to_remove - 1
#         view_groups()
#         group_to_remove = int(input('Enter the group you would like to remove the contact from: (select by number) '))
#         group_to_remove = group_to_remove - 1
#         group = groups[group_to_remove]
#         removed_contact = group.pop(contact_to_remove)
#         print(f'You have removed the contact: {removed_contact} from the group: {group}')
#     except ValueError:
#         print('Please enter a valid number.')
#     except IndexError:
#         print('Please enter a number within the available list parameters.')

# def display_contacts_in_group():
#     view_groups()
#     try:
#         group_to_display = int(input('Enter the group you would like to display: (select by number) '))
#         group_to_display = group_to_display - 1
#         group = groups[group_to_display]
#         print(f'Here are the contacts in the group: {group}')
#         for contact in group:
#             print(group.index(contact) +1, end=' ')
#             print(contact)
#     except ValueError:
#         print('Please enter a valid number.')
#     except IndexError:
#         print('Please enter a number within the available list parameters.')

def exit_program():
    backup_contacts()
    print('Thank you for using the Contact Management System. Goodbye!')
    quit()

#-----------------Main Program----------------

def main():
    while True:
        try:
            user_choice = int(input('''
                        WELCOME TO THE CONTACT MANAGEMENT SYSTEM
                                    1. Add a contact
                                    2. View all contacts
                                    3. Edit a contact
                                    4. Delete a contact
                                    5. Search for a contact
                                    6. Export contacts
                                    7. Import contacts
                                    8. Exit
                                    (Please enter the corresponding number for the action you'd like to take): '''))
            if user_choice == 1:
                clear()
                add_contact()
            elif user_choice == 2:
                clear()
                view_contacts()
            elif user_choice == 3:
                clear()
                edit_contact()
            elif user_choice == 4:
                clear()
                delete_contact()
            elif user_choice == 5:
                clear()
                search_contact()
            elif user_choice == 6:
                clear()
                export_contacts()
            elif user_choice == 7:
                clear()
                import_contacts()
            elif user_choice == 8:
                clear()
                exit_program()
        except ValueError:
            print('ValueError.')
        except IndexError:
            print('Please enter a number within the available list parameters.')
        except KeyError:
            print('KeyError.')
        except TypeError:
            print('TypeError.')
                                    

            
                   
                                    
                                    
      

main() # Call the main function to run the program