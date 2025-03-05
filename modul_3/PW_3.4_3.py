goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))

goods.append([fruit_name, price])
print(f'\nНовый ассортимент: {goods}')

# for index in range(len(goods)):
#     goods[index][1] = goods[index][1] + goods[index][1] * 8 / 100

for i_goods in goods:
    i_goods[1] = i_goods[1] + i_goods[1] * 8 / 100

print(f'\nНовый ассортимент с увел. ценой: {goods}')