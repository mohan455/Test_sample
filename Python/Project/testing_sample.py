import json

data = {
    "mohan":6303434200,
    "abc":4568923688
}
file_name="contact.json"
newentry = {
    "hello":8562378451,
    "hai":7856982532,
    "user":9875623487
}
name=input("enter name");
with open(file_name, 'r') as file:
    my_read_data = json.load(file)
    for key,value in my_read_data.items():
        if key==name:
            print("the contact name is already there")
            break

contact=int(input("enter contact"))
my_read_data[name]=contact

try:
    with open(file_name,'r') as file:
        my_read_data=json.load(file)
except FileNotFoundError:
    {}
my_read_data.update(data)
with open(file_name, 'w') as file:
    json.dump(data, file, indent=4)
with open(file_name, 'r') as file:
    my_read_data = json.load(file)
    for key,value in my_read_data.items():
        print(f"{key}-{value}")
