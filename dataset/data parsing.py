# csv2json
import csv
import json

csvFilePath = r'/Users/wangyue/Documents/project-files/dataset/restaurants_info.csv'
jsonFilePath = r'/Users/wangyue/Documents/project-files/dataset/restaurants_info.json'
# Call the make_json function

jsonArray = []

#read csv file
with open(csvFilePath, encoding='utf-8') as csvf:
    #load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf, delimiter=";")
    #convert each csv row into python dict
    for row in csvReader:
        #add this python dict to json array
        jsonArray.append(row)

#convert python jsonArray to JSON String and write to file
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonString = json.dumps(jsonArray, indent=4)
    jsonf.write(jsonString)

#jsonjoin accoridng to ID
listPath = r'/Users/wangyue/Documents/project-files/dataset/restaurants_list.json'
infoPath = jsonFilePath
totaljson = r'/Users/wangyue/Documents/project-files/dataset/totalrestaurantINFO.json'

import pandas as pd
import os

os.chdir(os.getcwd())
df1 = pd.read_json(listPath)
df2 = pd.read_json(infoPath)
df = pd.merge(df1, df2, on = "objectID")

#id and geo need to be intergers, no line
df.to_json(totaljson, index=False, orient='records')

#push to algolia
from algoliasearch.search_client import SearchClient

client = SearchClient.create("0ID4OD4XQ9", "ea507a8fa26bbc05662d550aad4de774")
index = client.init_index("restaurantINFO")

restaurants = json.load(open(totaljson))
index.save_objects(restaurants)

