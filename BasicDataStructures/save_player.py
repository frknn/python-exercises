print("Save Player")

name = input("enter name: ")
lastname = input("enter lastname: ")
team = input("enter team: ")

playerinfo = [name,lastname,team]

print("\nsaving your informations...\n")

print("Player name: {} \n"
      "Player last name: {} \n"
      "Player team: {} ".format(playerinfo[0], playerinfo[1], playerinfo[2]))

print("\ninfos saved...")
