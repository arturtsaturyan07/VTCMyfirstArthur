class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            return 'Enemy is already defeated'
        else:
            dist = ((actor.pos_x - target.pos_x) ** 2 + (actor.pos_y - target.pos_y) ** 2) ** 0.5
            if actor.weapon_on().range < dist:
                print(f'Enemy is too far for a weapon {actor.weapon_on}')
            else:
                print(f'Enemy has suffered damage by a weapon {actor.weapon_on().name} in the amount of {actor.weapon_on().damage}')
                target.get_damage(actor.weapon_on().)


    def __repr__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return (self.pos_x, self.pos_y)


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        self.weapon = weapon
        super().__init__(pos_x, pos_y, hp)

    def weapon_on(self):
        return self.weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)

    def __repr__(self):
        return f'Enemy in a position ({self.pos_x}, {self.pos_y}) with a weapon {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        self.name = name
        self.weapons = []
        super().__init__(pos_x, pos_y, hp)

    def weapon_on(self):
        if self.weapon:
            return self.weapon

    def hit(self, target):
        if isinstance(target, BaseEnemy):
            self.weapon.hit(self, target)
        else:
            print('I can hit only Enemy')

    def add_weapon(self):



    def next_weapon(self):
