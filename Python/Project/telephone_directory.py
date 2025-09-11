from creatingnew_contact import *

is_file_empty()
while 1:
    option=menu()
    if option== "quit" :
        break
    elif  option == "1":
        creatingnewcontact()
    elif option == "2":
        veiwcontacts()
    elif option == "3":
        searchcontact()
    elif option == "4":
        updatingcontact()
    elif option == "5":
        deletecontact()
    else:
        print("the user entered the wrong choice, select the right option")



