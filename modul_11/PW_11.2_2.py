class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 0

class Headphones:
    sensitivity = 108
    micro = True
    name = 'Sony'

monitor = [Monitor() for _ in range(4)]
headphone = [Headphones() for _ in range(3)]

for i_ind, i_freq in enumerate([60, 144, 70, 60]):
    monitor[i_ind].freq = i_freq
    print(monitor[i_ind].name, monitor[i_ind].matrix, monitor[i_ind].res, monitor[i_ind].freq)

try:
    for i_head in range(len(headphone)):
        headphone[0].micro = False
        print(headphone[i_head].name, headphone[i_head].micro, headphone[i_head].sensitivity)
except TypeError as err:
    print(err, type(err))
