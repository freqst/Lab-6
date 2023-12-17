from math import floor, ceil

class Character:
    className = 'The main character'

    def __init__(self, hp, ep, damage): #hp - health points; ep - endurance points
        self._hp = hp
        self._ep = ep
        self._damage = damage

    def fight(self):
        return floor(self._ep / self._damage)

class Weak_enemy(Character):
    className = "Weak enemy"

    def __init__(self, hp, ep, damage, inf): #inf - infection (слабый враг получает доп. урон по себе)
        super().__init__(hp, ep, damage)
        self._inf = inf

    def fight_death(self, character):
        return ceil(self._hp / (character._damage + self._inf))

class Boss(Character):
    className = "Boss"

    def __init__(self, hp, ep, damage, mg): #mg - magic (босс наносит доп урон герою)
        super().__init__(hp, ep, damage)
        self._mg = mg

    def fight_boss(self, character):
        return ceil(self._hp / character._damage)


print("Введите характеристики героя (очки здоровья, очки выносливости, урон): ")
hpC = int(input())
epC = int(input())
damageC = int(input())

character = Character(hpC, epC, damageC)
print(f"Вы: {Character.className}")
print(f'Вы можете нанести {character.fight()} ударов до изнеможения')


print("Введите характеристики слабого врага(очки здоровья, очки выносливости, урон, инфекция): ")
hpW = int(input())
epW = int(input())
damageW = int(input())
infW = int(input())

weak_enemy = Weak_enemy(hpW, epW, damageW, infW)
print(f'Сейчас драка с: {Weak_enemy.className}')
print(f'Понадобилось {weak_enemy.fight_death(character)} ударов до смерти врага')

print("Введите характеристики босаа (очки здоровья, очки выносливости, урон, магия): ")
hpB = int(input())
epB = int(input())
damageB = int(input())
mgB = int(input())

boss = Boss(hpB, epB, damageB, mgB)
print(f'Сейчас драка с: {Boss.className}')
print(f'Понадобилось {boss.fight_boss(character)} до смерти врага')