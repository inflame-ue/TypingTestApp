# TODO: Get random words from random-word-api.herokuapp.com(thanks RazorSh4rk for it)

# imports
import requests
import random


# function block
def get_data():
    """
    This function gets data from the random-word-api.com using requests library
    :return: list of random words
    """
    # parameters for the get request
    parameters = {
        "number": 300,
        "swear": 0,
    }

    # make a get request
    response = requests.get(url="https://random-word-api.herokuapp.com/word", params=parameters)
    response.raise_for_status()

    # return the data
    return response.json()


def write_data(data: list) -> None:
    """
    This function writes random words that we get from get_data function to the data/hard_mode.txt
    :param data: list of random words
    :return: None
    """
    # create 30 random sentences from the random worda that we got
    sentences = [" ".join(random.sample(data, 7)) for i in range(30)]

    # write them to a file
    with open("data/hard_mode.txt", "a") as file:
        for sentence in sentences:
            file.write(f"{sentence}\n")


write_data(get_data())
