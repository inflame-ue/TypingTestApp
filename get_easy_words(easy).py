# TODO: Create a function that will request random words from https://www.wordnik.com and then write it to easy_mode.txt

# imports
import requests
import dotenv
import os
import random


# function block
def get_random_words() -> list:
    """
    This function sends a GET request to wordnik API in order to get a query of random words
    :return: query of random words
    """
    # parameters for the request
    dotenv.load_dotenv("C://EnvironmentalVariables//.env")
    parameters = {
        "api_key": os.environ.get("API_KEY"),
        "hasDictionaryDef": True,
        "minLength": 4,
        "maxLength": 8,
        "limit": 300,
    }

    # send a GET request
    response = requests.get("https://api.wordnik.com/v4/words.json/randomWords", params=parameters)
    response.raise_for_status()

    # return data as a list of words
    data = [dictionary["word"] for dictionary in response.json()]
    return data


def write_data_to_easy_mode_txt(data: list) -> None:
    """
    This function writes the words that we got from wordnik API to data/easy_mode.txt
    :param data: list of words that we need to write to a file
    :return: None
    """
    # create a bunch of random sentences
    sentences = [" ".join(random.sample(data, 7)) for i in range(30)]

    # write them to an easy_mode.txt
    with open("data/easy_mode.txt", "a", encoding="utf-8") as file:
        for sentence in sentences:
            file.write(f"{sentence}\n")


write_data_to_easy_mode_txt(get_random_words())
