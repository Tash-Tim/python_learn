class Toyota:

    def __init__(self, color = 'red', price = 1000000, max_speed = 200):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.curr_speed = 0

    def car_info(self):
        print('Car color: {}\nCar price: {}\nCar max speed: {}\nCar curr speed: {}\n'.
              format(self.color, self.price, self.max_speed, self.curr_speed))

    def car_curr_speed(self, curr_speed=0):
        self.curr_speed = curr_speed
        self.car_info()


corola = Toyota('green', 1200000, 220)
camry = Toyota('white', 1500000, 260)
yaris = Toyota()

corola.car_curr_speed(120)
camry.car_curr_speed(150)
yaris.car_curr_speed()
