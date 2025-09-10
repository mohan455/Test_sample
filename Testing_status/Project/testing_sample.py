with open('contact_directory.txt','r+') as file:
    content=file.readlines()
    for i in range(len(content)):
        update_contact=content[i].split("-")
        if update_contact[0]=="mohan":
            update_contact[0]="sai"
            content[i] = "-".join(update_contact) + "\n"

    file.seek(0)
    file.writelines(content)
    file.truncate()






        #if duplicate[0].strip()=="mohan":

