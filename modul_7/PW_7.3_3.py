def data_check(input_data):
    result = list()
    if isinstance(input_data, dict):
        input_data = input_data.values()
    elif isinstance(input_data, set):
        input_data = list(input_data)

    result = [i_elem for i_inde, i_elem in enumerate(input_data)  if i_inde % 2 == 0 ]

    return result


data_1 = 'О Дивный Новый мир!'
dete_2 = [100, 200, 300, 'буква', 0, 2, 'а']
data_3 = {0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}

print(data_check(data_1))
print(data_check(dete_2))
print(data_check(data_3))