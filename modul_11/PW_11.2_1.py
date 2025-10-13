import random

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    curr_speed = 0

# corola = Toyota()
# camty = Toyota()
# yaris = Toyota()

# corola.curr_speed = random.randint(0, 200)
# camty.curr_speed = random.randint(0, 200)
# yaris.curr_speed = random.randint(0, 200)

# print('Data of Corolla:', corola.price, corola.color, corola.max_speed, corola.curr_speed)
# print('Data of Camry:', camty.price, camty.color, camty.max_speed, camty.curr_speed)
# print('Data of Yaris:',yaris.price, yaris.color, yaris.max_speed, yaris.curr_speed)

car_tuple = ('corola', 'camry', 'yaris', 'Prado', 'Supra')
cars = [Toyota() for _ in range(len(car_tuple))]
for i_ind, i_car in enumerate(car_tuple):
    cars[i_ind].curr_speed = random.randint(0, 200)
    print('{i} data: {}'.format((cars[i_ind].color, cars[i_ind].price, cars[i_ind].max_speed,
                                    cars[i_ind].curr_speed), i=i_car))
