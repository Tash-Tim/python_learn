def create_dict(i_elem, template=None):
    if isinstance(i_elem, dict):
        return i_elem
    elif isinstance(i_elem, (int, float, str)):
        template = template or dict()
        template[i_elem] = i_elem
        return template
    else:
        return None


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_elem = create_dict(i_element)
        if new_elem:
            new_list.append(new_elem)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)

