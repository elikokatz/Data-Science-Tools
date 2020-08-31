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


def check_dir(udir):
    for fn in os.listdir(udir):
        with open(udir + "/" + fn) as file:
            if not is_json_file(file):
                return False
    return True


user_dir = input("Directory with json files: ")
if not check_dir(user_dir):
    print("Non valid json file(s) found")
else:
    features = []
    ft = input("Enter desired feature from json file (enter -1 to terminate): ")
    while ft != "-1":
        features.append([ft, pd.Series([], dtype=object)])
        ft = input("Enter desired feature from json file (enter -1 to terminate): ")

    for filename in os.listdir(user_dir):
        with open(user_dir + "/" + filename) as json_file:
            data = json.load(json_file)
            for ft in features:
                ft[1] = ft[1].append(pd.Series(data[ft[0]]), ignore_index=True)

    user_dir = input("Enter the desired directory to output the csv file to: ")
    name = input("Enter the desired file name: ")
    path = user_dir + "/" + name + ".csv"

    column_headers = features[0][0]
    for i in range(1, len(features)):
        column_headers += "," + features[i][0]

    lst = []
    rows = []
    for i in range(features[0][1].size):
        for j in range(len(features)):
            lst.append(features[j][1][i])
        rows.append(lst)
        lst = []

    df = pd.DataFrame(data=rows, columns=column_headers.split(","))
    df.to_csv(path_or_buf=path)

