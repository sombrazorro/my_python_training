def reshape(data_list, step):
    result = []
    while data_list != data_list[:step]:
        result.append(data_list[:step])
        data_list = data_list[step:]
    return result

def format_hex(bytes_data_list):
    count = 0
    for x in bytes_data_list:
        print(f"{count:07x}", end="")
        
