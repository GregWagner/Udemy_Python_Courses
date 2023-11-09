from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

greg = Player("Greg")

print(greg.name)
print(greg.lives)

greg.lives -=1
print(greg)

greg.lives -=1
print(greg)

greg.lives -=1
print(greg)

greg.lives -=1
print(greg)

greg.level = 2
print(greg)

greg.level += 5
print(greg)

greg.level = 3
print(greg)

greg.score = 123
print(greg)

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

troll_1 = Troll("Pug")
print(troll_1)

troll_2 = Troll("Ug")
troll_3 = Troll("Urg")
troll_1.grunt()

print("*" * 20)
vamp = Vampyre("Count Burt")
print(vamp)

while vamp.alive:
    vamp.take_damage(3)
    print(vamp)

king = VampyreKing("The King")
king.take_damage(4)
print(king)
