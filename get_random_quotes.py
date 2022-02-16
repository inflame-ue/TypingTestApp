# TODO: Get random quotes from https://github.com/lukePeavey/quotable. It will be used in the medium mode of the game

# imports
import requests
import random


# function block
def get_random_quotes():
    """
    This function uses requests module to get random quotes from the API
    :return: json, which contains all quotes
    """
    # params for the request
    parameters = {
        "page": 1,
        "limit": 150
    }

    # make a GET request
    response = requests.get(url="https://api.quotable.io/quotes", params=parameters)
    response.raise_for_status()

    # return data
    return response.json()


def write_data_to_medium_mode_txt(data):
    """
    This function takes data that we got from the random quotes API and writes it to medium_mode.txt
    :param data: random quotes that we got from the API call
    :return: nothing
    """
    pass