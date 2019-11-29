class Entity:
    def __init__(self,health):
        self.health = health


class Player(Entity):
    def __init__(self,health,power):
        super().__init__(health)
        self.power = power
        print("New player created.\nHealth:{}\nPower:{}\n".format(self.health,self.power))

    def attack(self,enemy_object):
        print("I'm attacking to", enemy_object)
        enemy_object.health -= self.power
        print("Dealt {} damage to enemy\nEnemy has {} HP left".format(self.power,enemy_object.health))


    def heal(self):
        print("I'm healing myself!")
        self.health += 15
        print("Added 15 to my health. My health is now",self.health)


class Enemy1:
    health = 100
    power = 10

    def __init__(self):
        print("New Enemy1 created.\nHealth:{}\nPower:{}\n".format(self.health,self.power))

    def attack_player(self,player):
        if not isinstance(player, Player):
            print("Can't attack my ally")
        else:
            print("Enemy1 attacks you back!\nYou take {} damage".format(self.power))
            player.health -= self.power
            print(str(player.health) + " HP left")


class Enemy2:
    health = 200
    power = 8

    def __init__(self):
        print("New Enemy2 created.\nHealth:{}\nPower:{}\n".format(self.health,self.power))

    def attack_player(self,player):
        if not isinstance(player, Player):
            print("Can't attack my ally")
        else:
            print("Enemy2 attacks you back!\nYou take {} damage".format(self.power))
            player.health -= self.power
            print(str(player.health) + " HP left")


player1 = Player(150,15)
enemy1 = Enemy1()
enemy2 = Enemy2()

while True:
    print("\n1 -> ATTACK || 2 -> HEAL")
    key = int(input("Make your choice: "))
    if key == 2:
        player1.heal()
    elif key == 1:
        print("Enemy 1 or Enemy 2?")
        enemy_select = int(input())
        if enemy_select == 1:
            player1.attack(enemy1)
            enemy1.attack_player(player1)
        else:
            player1.attack(enemy2)
            enemy2.attack_player(player1)
    if enemy1.health <= 0 and enemy2.health <= 0:
        print("Congrats! You win!")
        break
    elif player1.health <= 0:
        print("You died! Game over!")
        break
