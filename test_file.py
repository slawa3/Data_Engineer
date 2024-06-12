
import yaml

dict_file = [
    {
        'user_name': 'Vyacheslav',
        'password': '12345'
    },
    {
        'user_name': 'Vasya1',
        'password': '54321'
    }
]


with open('connect.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)


with open('connect.yaml') as file:
    connections = yaml.load(file, Loader=yaml.FullLoader)
    print(connections)
    print(type(connections))


import json

dict2 = {
    'name': 'Petya',
    'rollno': 5,
    'age': 25,
    'phone_number': '987565656'
}

json_obj = json.dumps(dict2, indent = 4)

a = [1,2,3,4]

with open('dict.json', 'w') as outfile:
    outfile.write(json_obj)

b = [1,2,3,4]