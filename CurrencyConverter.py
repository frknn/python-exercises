import requests

api_key = "b1015565d2acd8c81ceeda5a5d53e126"


first_curr = input("Which currency do you want to convert: ")
second_curr = input("Which curr do you want to convert to: ")
amount = input("Enter amount: ")

url = "http://data.fixer.io/api/latest" + "?access_key=" + api_key + "&symbols=" + first_curr + "," + second_curr

response = requests.get(url)
my_json = response.json()


eur_amount = float(amount) * (1/float(my_json['rates'][first_curr]))
wanted_amount = eur_amount * float(my_json['rates'][second_curr])

print(str(amount), first_curr, "=", wanted_amount, second_curr)

# print(my_json['rates'][first_curr],my_json['rates'][second_curr])

