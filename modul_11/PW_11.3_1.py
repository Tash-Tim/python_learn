class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    curr_speed = 0

    def car_info(self):
        print('Car color: {}\nCar price: {}\nCar max speed: {}\nCar curr speed: {}\n'.
              format(self.color, self.price, self.max_speed, self.curr_speed))

    def car_curr_speed(self):
        self.curr_speed = input('Set current speed: ')


car_tpl = ('corola', 'camry', 'yaris')

toyota_cars = [Toyota() for _ in range(len(car_tpl))]

for car_ind, car_name in enumerate(car_tpl):
    toyota_cars[car_ind].car_curr_speed()
    print(car_name, 'data:')
    toyota_cars[car_ind].car_info()


