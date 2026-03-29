#serialization or encoding
import json
person = {    "firstName":"Hamidur Rahman",
    "lastName":"Majed",
    "hobbies":["running","swimming","singing"],
    "age":28,
    "hasChildren":True,
    "children":[
        {
            "firstName":"Azad",
            "age":5,
        },
        {
            "firstName": "Bob",
            "age":7
        }

    ]}
perjson = json.dumps(person,indent=4,separators=('; ','= '))#separator is not recommended

# with open('person.json','r+') as file:
#     json.dump(person,file, indent=4)
# #line 19 and 21 are same
# #deserialization

#     person = json.loads('person.json')
#     print(person)
with open('person.json','r') as file:
    person = json.load(file)
    print(person)
def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('not a json')
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User('Max',27)
userjson = json.dumps(user,default=encode_user)
print(userjson)