from enum import Enum
from random import randint, choice


class Ability(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    STUN = 5
    HACKING = 6
    RANGE = 7
    THROW_SHURIKEN = 8


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None
        self.__skiped_rounds = 0

    @property
    def defence(self):
        return self.__defence

    @property
    def skiped_rounds(self):
        return self.__skiped_rounds

    @skiped_rounds.setter
    def skiped_rounds(self, value):
        if value > 0:
            self.__skiped_rounds = value

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.super_ability

    def attack(self, heroes):
        if self.__skiped_rounds > 0:
            self.__skiped_rounds -= 1
            return

        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS defence: {self.__defence} ' + super().__str__()


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior hits critically {self.damage * coeff}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_level):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_level = heal_level

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if self != hero and hero.health > 0:
                hero.health += self.__heal_level
        print('Medic heals')


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.STUN)

    def apply_super_power(self, boss, heroes):
        boss.skiped_rounds += 1
        print(f'Thor causes the boss to skip the round!')


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.HACKING)

    def apply_super_power(self, boss, heroes):
        another_heroes = [hero for hero in heroes if hero != self]
        damage_and_heal = randint(1, 5)
        boss.health -= damage_and_heal
        hero = choice(another_heroes)
        hero.health += damage_and_heal
        print(f'Hacker hacks boss health and cures {hero.name}')


class Magical(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        magic_boost = randint(3, 7)

        for hero in heroes:
            if hero == self:
                continue

            hero.damage += magic_boost
            print(f'Magical increases the damage of teammates')


class Deku(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.RANGE)

    def apply_super_power(self, boss: Boss, heroes):
        range_levels = [20, 50, 100]
        current_range = choice(range_levels)

        if current_range == 20:
            boss.health -= self.damage * 0.2
        if current_range == 50:
            boss.health -= self.damage * 0.5
        if current_range == 100:
            boss.health -= self.damage
        print(f'Deku falls into a range!')


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.THROW_SHURIKEN)

    def apply_super_power(self, boss, heroes):
        shuriken_types = ['toxic', 'pill']
        current_shuriken = choice(shuriken_types)
        shuriken_power = randint(1, 20)

        if current_shuriken == 'toxic':
            boss.health -= shuriken_power
        if current_shuriken == 'pill':
            boss.health += shuriken_power
        print('Samurai throws shuriken')


round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')
        return True

    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0:
            hero.attack(boss)
    hero = choice(heroes)
    if boss.defence != hero.super_ability:
        hero.apply_super_power(boss, heroes)

    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Hitler', 1000, 20)

    warrior = Warrior('Arthur', 280, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    assistant = Medic('Aivo', 290, 5, 5)
    god_of_thunder = Thor('Thor', 300, 10)
    cool_hacker = Hacker('Vovochka', 100, 3)
    magic = Magical('Merlin', 270, 20)
    konan_deku = Deku('Konan', 200, 15)
    jeck_samurai = Samurai('Jeck', 280, 18)

    heroes_list = [warrior, doc, assistant,
                   god_of_thunder, cool_hacker, magic, konan_deku, jeck_samurai]

    show_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


start_game()