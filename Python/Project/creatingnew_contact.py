
def menu():
    user_choice=input("enter the choice\n "
                "1 for creating a contact\n"
                  "2 for viewing the contacts\n"
                  "3 for searching\n"
                  "4 for updating\n"
                  "5 for deleting\n")
    return user_choice

def is_file_empty():
    with open('contact_directory.txt', 'r') as file:
        file_empty_check = file.read(1)
        if not file_empty_check:
            print("the file is empty,please add the contact first")
            creatingnewcontact()


def creatingnewcontact():
    contact_name = input("enter the name \n")
    contact_number = input("enter the contact_number\n")
    with open('contact_directory.txt', 'r') as file:
        file_content_check = file.readlines()
        for item in file_content_check:
            duplicate_check= item.split("-")
            if duplicate_check[0].strip()==contact_name:
                print("the contact is already there,try with different details")
                creatingnewcontact()
    with open('contact_directory.txt','a') as file:
                if contact_name == "" or len(contact_number)>10 or len(contact_number)<10:
                        print("the contact details are not valid::, enter the valid details")
                        creatingnewcontact()
                elif contact_number.startswith("0") or contact_number.startswith("1") or contact_number.startswith("2") or contact_number.startswith("3") or contact_number.startswith("4") or contact_number.startswith("5"):
                        print("the contact details are not valid, enter the valid details")
                        creatingnewcontact()
                elif len(contact_name)<=50 and len(contact_number)==10:
                        if contact_number.startswith("6") or contact_number.startswith("7") or contact_number.startswith("8") or contact_number.startswith("9"):
                            file.write(contact_name + " - " + contact_number + "\n")
                            print("the contact saved successfully")

def veiwcontacts():
    with open('contact_directory.txt', 'r') as file:
        file_empty_check = file.read(1)
        if not file_empty_check:
            print("the file is empty,please add the contact first")
            creatingnewcontact()
    try:
        file_open=open('contact_directory.txt','r')
        content=file_open.readlines()
        for i in content:
            print(f"the file content is ",{i})
        file_open.close()
    except FileNotFoundError:
        print("the file is not found")

def searchcontact():
    contact_search=input("enter the contact to be searched\n")
    with open('contact_directory.txt','r') as file:
        content=file.readlines()
        for item in content:
            actual_contact=item.split("-")
            if actual_contact[0].strip()==contact_search:
                print(f"the contact found and the details are:",{item})
                break
        else:
            print("the contact was not there for search,please try adding again and search")

def updatingcontact():
    contact_update = input("enter the contact name for the update\n")
    with open('contact_directory.txt', 'r+') as file:
        content = file.readlines()
    with open('contact_directory.txt','w') as file:
        for item in content:
            duplicate=item.split("-")
            if duplicate[0].strip==contact_update:
                duplicate[0]=contact_update
                file.write(item)
                break



def deletecontact():
    contact_remove = input("enter the contact name to remove\n")
    with open('contact_directory.txt', 'r') as file:
        content = file.readlines()
    with open('contact_directory.txt', 'w') as file:
        for item in content:
            duplicate=item.split("-")
            if not duplicate[0].strip()==contact_remove:
                file.write(item)
            elif duplicate[0].strip()==contact_remove:
                print("the contact removed successfully")
            else:
                print("the contact is not found for deletion")
