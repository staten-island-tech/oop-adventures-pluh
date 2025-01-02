class user:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.buff = 0

    def buy(self, item):
        self.items.append(item)
        print(f"you bought a {item}.")

    def attack(self, enemy):
        total_damage = 10 + self.buff
        enemy.hp -= total_damage
        print(f"you attacked {enemy.name} for {total_damage} damage.")


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp