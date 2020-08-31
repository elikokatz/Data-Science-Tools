import numpy as np
import pandas as pd
import json
import os


def is_json_file(file):
    try:
        json.load(file)
    except ValueError:
        return False
    return True


def check_dir(user_dir):
    for filename in os.listdir(user_dir):
        with open(user_dir + "/" + filename) as file:
            if not is_json_file(file):
                return False
    return True


user_dir = input("Directory with json files: ")
print(check_dir(user_dir))
