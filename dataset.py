import pandas as pd

df = pd.read_csv('Food List.csv')  # to read csv file


def stall_type():
    """convert type of stalls in food list.csv to list

    return:
    stall_type_list: list
        result of conversion of data retrieved from csv file to list
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
    """Convert data into dictionary

    Parameter:
    list_menu: list
        key in this dictionary
    food_price: list
        is value in this dictionary
    delivery_services: list
        is value in this dictionary
    
    return:
    food_dict: Dictionary
        result of converting list to dictionary
    """
    # Step 1: Zip all the data using zip()
    # Step 2: declare a dictionary
    zipfile = zip(list_menu, food_price, delivery_service)
    food_dict = {}

    # Step 3: Using for loop to update dictionary
    for i, j, k in zipfile:
        food_dict[i] = [j, k]
    return food_dict


def malay_data():
    """convert data in food list.csv file to list and string using pandas library

    return:
    item_menu: string
        result of conversion of data retrieved from csv file to string from row 0 to row 12
    list_menu: list
        result of conversion of data retrieved from csv file to string from row 0 to row 12
    food_price: list
        result of conversion of data retrieved from csv file to string from row 0 to row 12

    """
    item_name = df['item_name'][0:13].to_string()
    list_menu = df['item_name'][0:13].tolist()
    food_price = df['price'][0:13].tolist()
    delivery_service = df['delivery_service'][0:13].tolist()
    return item_name, list_menu, food_price, delivery_service


def mamak_data():
    """convert data in food list.csv file to list and string using pandas library

    return:
    item_menu: string
        result of conversion of data retrieved from csv file to string from row 13 to row 31
    list_menu: list
        result of conversion of data retrieved from csv file to string from row 13 to row 31
    food_price: list
        result of conversion of data retrieved from csv file to string from row 13 to row 31

    """
    item_name = df['item_name'][13:32].to_string()
    list_menu = df['item_name'][13:32].tolist()
    food_price = df['price'][13:32].tolist()
    delivery_service = df['delivery_service'][13:32].tolist()
    return item_name, list_menu, food_price, delivery_service


def beverages_data():
    """convert data in food list.csv file to list and string using pandas library

    return:
    item_menu: string
        result of conversion of data retrieved from csv file to string from row 32 to row 46
    list_menu: list
        result of conversion of data retrieved from csv file to string from row 32 to row 46
    food_price: list
        result of conversion of data retrieved from csv file to string from row 32 to row 46

    """
    item_name = df['item_name'][32:47].to_string()
    list_menu = df['item_name'][32:47].tolist()
    food_price = df['price'][32:47].tolist()
    delivery_service = df['delivery_service'][32:47].tolist()
    return item_name, list_menu, food_price, delivery_service


def korean_data():
    """convert data in food list.csv file to list and string using pandas library

    return:
    item_menu: string
        result of conversion of data retrieved from csv file to string from row 47 to row 62
    list_menu: list
        result of conversion of data retrieved from csv file to string from row 47 to row 62
    food_price: list
        result of conversion of data retrieved from csv file to string from row 47 to row 62

    """
    item_name = df['item_name'][47:62].to_string()
    list_menu = df['item_name'][47:62].tolist()
    food_price = df['price'][47:62].tolist()
    delivery_service = df['delivery_service'][47:62].tolist()
    return item_name, list_menu, food_price, delivery_service


def japanese_data():
    """convert data in food list.csv file to list and string using pandas library

    return:
    item_menu: string
        result of conversion of data retrieved from csv file to string from row 62 to row 86
    list_menu: list
        result of conversion of data retrieved from csv file to string from row 62 to row 86
    food_price: list
        result of conversion of data retrieved from csv file to string from row 62 to row 86

    """
    item_name = df['item_name'][62:87].to_string()
    list_menu = df['item_name'][62:87].tolist()
    food_price = df['price'][62:87].tolist()
    delivery_service = df['delivery_service'][62:87].tolist()
    return item_name, list_menu, food_price, delivery_service




