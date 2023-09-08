
class Auto:
    def __init__(self, brand, color, volume):
        self.brand : str = None
        self.color : str = None
        self.volume : float = None

    def drive_forward(self):
        print('Їду вперед')
    
    def drive_back(self):
        print('Їду назад')
    
    def __str__(self):
        return f'{self.__class__}: Марка - {self.brand}. Колір - {self.color}. Об`єм - {self.volume}'


class NewAuto(Auto):
    def turn_left(self):
        print('Повертаю ліворуч')
    
    def turn_right(self):
        print('Повертаю праворуч')
    

class Plane:
    def __init__(self, brand):
        self.brand : str = None


    def takeoff(self):
        print('Літак взлітає')
    

class IdkWhatIsIt(NewAuto, Plane):
    pass



auto = Auto('BMW', 'Gray', 3.6)

auto.drive_forward()
auto.drive_back()

new_auto = NewAuto('Mercedes', 'White', 5.4)

new_auto.drive_forward()
new_auto.drive_back()
new_auto.turn_right()
new_auto.turn_left()

plane = Plane('Airbus')

plane.takeoff()

thing = IdkWhatIsIt('Mercedes', 'White', 5.4)

thing.drive_forward()
thing.drive_back()
thing.turn_right()
thing.turn_left()
thing.takeoff()