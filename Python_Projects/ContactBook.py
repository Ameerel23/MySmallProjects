import re

activity = True
contact_list = []

while activity == True:

    final_decision = True
    validity = True
    first_name = input("Enter your first name. ")
    last_name = input("Enter your last name. ")
    phone_number = input("Enter your 8 digit phone number. ")

    for x in first_name:
        if x.isalpha() == True:
            continue
        else:
            print("Invalid first name")
            validity = False
            break

    for y in last_name:
        if y.isalpha() == True:
            continue
        else:
            print("Invalid last name")
            validity = False
            break

    if len(phone_number) == 8:
        for z in phone_number:
            if z.isdigit() == True:
                continue
            else:
                print("Invalid phone number")
                validity = False
                break
    else:
        print("Insufficient digits")
        validity = False

    if validity == True:
        contact = [first_name, last_name, phone_number]
        contact_list.append(contact)
        print(contact_list)
    
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
