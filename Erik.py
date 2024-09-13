# write your code here
class Restaurant:
    mydict = dict()

    def __init__(self, name, times):
        self.name = name
        self.times = times

    def make_reservation(self, names, timm, data):
        if (not f'{timm} {data}' in self.mydict.keys()) and  self.times  - timm >= 0:
            self.mydict[f'{timm} {data}'] = names
            self.times -= timm
            print(f'Reservation made for {names} at {data}')
        else:
            print('No seats available')

    def order_food(self, *foods):
        print('Order with ' + ', '.join(foods) + ' placed!')


class FastFoodRestaurant(Restaurant):
    def make_reservation(self, names, timm, data):
        print('We do not take reservations.')




# FROZEN_SECTION_START
if __name__ == '__main__':
    exec(input())