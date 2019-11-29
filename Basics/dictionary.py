#A dict is basically an object in javascript

person = {
    "name": "Furkan",
    "lastname": "Setbaşı",
    "age": 20
}

print(person["name"])

#Adding a key to dict

person["phone"] = "555-55-55"
print(person["phone"])

#get keys of dict(elements of object)
print(person.keys())

#get items of dict
print(person.items())

#copy dict
person2 = person.copy()
person2["city"] = "karabük"
print(person2)

#removeing items
del(person["age"])
person.pop("phone")
print(person)

#list of dicts(like array of objects)
people = [
    {"name": "Furkan", "age":20},
    {"name": "Hakan", "age":17}
]

print(people[1]["age"])
