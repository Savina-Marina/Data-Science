def data_types():
    my_int = 1
    my_str = "Marina"
    my_float = 1.2
    my_bool = True
    my_list = [1, 2, 3]
    my_dict = {"name": "marina"}
    my_tuple = (4, 5, 6)
    my_set = {7, 8, 9} 

    res = [
        type(my_int).__name__, type(my_str).__name__, type(my_float).__name__, type(my_bool).__name__, 
        type(my_list).__name__, type(my_dict).__name__, type(my_tuple).__name__, type(my_set).__name__
    ]

    res_v  = str(res).replace("'", "")
    print(res_v)

if __name__ == '__main__':
    data_types()