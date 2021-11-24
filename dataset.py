import pandas as pd

df = pd.read_csv('Food List.csv')  # to read csv file


def stall_type():
    """
    this function is used to convert type of stalls in food list.csv to list
    then return stall_type_list to main.py
    """
    stall_type_list = [
            df['stall_name'][0],
            df['stall_name'][13],
            df['stall_name'][32],
            df['stall_name'][47],
            df['stall_name'][62]
            ]
    return stall_type_list


def to_dict(list_menu, food_price, delivery_service):
    """
    this function is used to convert data into dictionary
    list_menu will be key, while food_price and delivery_service will be values in list format
    """

    zipfile = zip(list_menu, food_price, delivery_service)
    food_dict = {}
    for i, j, k in zipfile:
        food_dict[i] = [j, k]
    return food_dict


def malay_data():
    """
    this function is used to convert data in food list.csv file to list and string using
    pandas library
    then return to main.py
    """
    item_name = df['item_name'][0:13].to_string()
    list_menu = df['item_name'][0:13].tolist()
    food_price = df['price'][0:13].tolist()
    delivery_service = df['delivery_service'][0:13].tolist()
    return item_name, list_menu, food_price, delivery_service


def mamak_data():
    """
    this function is used to convert data in food list.csv file to list and string using
    pandas library
    then return to main.py
    """
    item_name = df['item_name'][13:32].to_string()
    list_menu = df['item_name'][13:32].tolist()
    food_price = df['price'][13:32].tolist()
    delivery_service = df['delivery_service'][13:32].tolist()
    return item_name, list_menu, food_price, delivery_service


def beverages_data():
    """
    this function is used to convert data in food list.csv file to list and string using
    pandas library
    then return to main.py
    """
    item_name = df['item_name'][32:47].to_string()
    list_menu = df['item_name'][32:47].tolist()
    food_price = df['price'][32:47].tolist()
    delivery_service = df['delivery_service'][32:47].tolist()
    return item_name, list_menu, food_price, delivery_service


def korean_data():
    """
    this function is used to convert data in food list.csv file to list and string using
    pandas library
    then return to main.py
    """
    item_name = df['item_name'][47:62].to_string()
    list_menu = df['item_name'][47:62].tolist()
    food_price = df['price'][47:62].tolist()
    delivery_service = df['delivery_service'][47:62].tolist()
    return item_name, list_menu, food_price, delivery_service


def japanese_data():
    """
    this function is used to convert data in food list.csv file to list and string using
    pandas library
    then return to main.py
    """
    item_name = df['item_name'][62:87].to_string()
    list_menu = df['item_name'][62:87].tolist()
    food_price = df['price'][62:87].tolist()
    delivery_service = df['delivery_service'][62:87].tolist()
    return item_name, list_menu, food_price, delivery_service







