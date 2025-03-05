zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(zoo.index('lion') + 1, 'bear')
zoo.remove('elephant')
print(f'Зоопарк: {zoo}')
print(f'Лев сидит в клетке номер: {zoo.index('lion') + 1}')
print(f'Обезьяна сидит в клетке номер: {zoo.index('monkey') + 1}')