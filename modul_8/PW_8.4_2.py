def get_data_info(user_data):
    if isinstance(user_data, (list, dict, set)):
        user_data_mut = 'Изменяемый (mutable)'
    else:
        user_data_mut = 'Неизменяемый (immutable)'

    data_type_dict ={"<class 'str'>": "строка",
                    "<class 'tuple'>": "кортеж",
                    "<class 'dict'>": "словарь",
                    "<class 'list'>": "список",
                    "<class 'set'>": "множество"}
    user_data_type = data_type_dict[str(type(user_data))]

    return type(user_data), user_data_type, user_data_mut, id(user_data)

input_data =  {10, 20, 30}
tada_type, data_type_txt, data_mutable, data_id = get_data_info(input_data)

print(f'''Тип данных: {tada_type} ({data_type_txt})
{data_mutable}
id объекта: {data_id}''')