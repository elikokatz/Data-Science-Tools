import numpy as np
import pandas as pd
import json
import os

# Used to check if a file is a json file by checking the format 
def is_json_file(file):
    try:
        json.load(file)
    except ValueError:
        return False
    return True

# Used to check the directory for any non json files
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
    # Create a list of features.
    # Each object is a list containing a feature name in the first position and the corresponding pandas Series in the second position
    features = []
    ft = input("Enter desired feature from json file (enter -1 to terminate): ")
    while ft != "-1":
        features.append([ft, pd.Series([], dtype=object)])
        ft = input("Enter desired feature from json file (enter -1 to terminate): ")

    # Iterate over each file in the directory and append the corresponding data to the Series
    for filename in os.listdir(user_dir):
        with open(user_dir + "/" + filename) as json_file:
            data = json.load(json_file)
            for ft in features:
                ft[1] = ft[1].append(pd.Series(data[ft[0]]), ignore_index=True)
    
    # Ask the user for the desired directory and file name and then create the path
    user_dir = input("Enter the desired directory to output the csv file to: ")
    name = input("Enter the desired file name: ")
    path = user_dir + "/" + name + ".csv"

    # Create the column headers. Example: "first,second,third"
    column_headers = features[0][0]
    for i in range(1, len(features)):
        column_headers += "," + features[i][0]
    
    # Create the rows. Example: [[1, 2, 3], [3, 2, 1], [2, 1, 3]] where each list object is a row of the corresponding data
    lst = []
    rows = []
    for i in range(features[0][1].size):
        for j in range(len(features)):
            lst.append(features[j][1][i])
        rows.append(lst)
        lst = []
    
    # Convert the pandas DataFrame to a csv and save it on the desired path
    df = pd.DataFrame(data=rows, columns=column_headers.split(","))
    df.to_csv(path_or_buf=path)

