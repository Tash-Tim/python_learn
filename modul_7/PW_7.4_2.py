server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_kye, i_value in server_data.items():
    print(f'{i_kye}:')
    for j_name, j_value in i_value.items():
        print(f'\t{j_name} : {j_value}')
