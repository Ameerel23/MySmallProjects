import re

activity = True
contact_list = []  # List of contacts

#  Add contacts
while activity == True:

    print('Contacts:', contact_list)
    #  Boolean variables to validate new contact
    final_decision = True
    validity = True

    #  Add one contact at a time
    first_name = input("Enter your first name. ")
    last_name = input("Enter your last name. ")
    phone_number = input("Enter your 8 digit phone number. ")

    #  Validate first name
    for first_name_check in first_name.replace(" ", ""):
        if first_name_check.isalpha() == True:
            continue
        else:
            print("Invalid first name")
            validity = False
            break

    #  Validate last name
    for last_name_check in last_name.replace(" ", ""):
        if last_name_check.isalpha() == True:
            continue
        else:
            print("Invalid last name")
            validity = False
            break

    #  Validate phone number
    if len(phone_number) == 8:
        for digit in phone_number:
            if digit.isdigit() == True:
                continue
            else:
                print("Invalid phone number")
                validity = False
                break

        for duplicate_finder in contact_list:
            if duplicate_finder[2] == phone_number:
                print("Phone number is already used.")
                validity = False
                break

    else:
        print("Insufficient digits")
        validity = False

    #  Add validated contact details to the list
    if validity == True:
        contact = [first_name, last_name, phone_number]
        contact_list.append(contact)
        print(contact_list)

    #  Ask user if he/she would like another contact to be added
    while final_decision == True:
        decision = input("Would you like to add another contact number (Y/N)? ")
        if decision.lower() == "y" or decision.lower() == "yes":
            final_decision = False
            continue
        
        elif decision.lower() == "n" or decision.lower() == "no":
            final_decision = False
            activity = False

        else:
            print("Your response was not understood. Please select Y/N")
