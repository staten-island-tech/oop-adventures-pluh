class User:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.buff = 0

    def attack(self, enemy):
        total_damage = 10 + self.buff
        enemy.hp -= total_damage
        print(f"You attacked {enemy.name} for {total_damage} damage.")

class Shop:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def sell(self, item, user):
        if item in self.products:
            self.products.remove(item)
            user.items.append(item)
            print(f"You bought {item}.")
            print(f"Your items: {user.items}")
            print(f"products in shop: {self.products}")
        else:
            print(f"{item} is not available in the shop.")

    def apply_buff(self, user):
        user.buff += 10

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

user1 = User("lucas", [])
shop1 = Shop("Weapon Shop", ["Sword", "Shield", "Bow", "Banana"])
enemy1 = Enemy("tribe guy", 50)

shop1.sell("Sword", user1)
user1.attack(enemy1)
shop1.apply_buff(user1)
user1.attack(enemy1)