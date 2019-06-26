'''
TODO:
- Print out the exact matches
- BUG: searching "Budweiser" yields "Bud Light" as first result and "Budweiser" second.
       figure out a way to search for exact match
'''

import os
import csv
import json
import requests

config_path = os.path.join("..", "config.json")

with open(config_path) as json_data_file:
    config_data = json.load(json_data_file)

untappd_id = config_data["untappd_api"]["client_id"]
untappd_secret = config_data["untappd_api"]["client_secret"]
untappd_url_beer_search = "https://api.untappd.com/v4/search/beer"

beer_search_params = {
    "q": "",
    "client_id": untappd_id,
    "client_secret": untappd_secret
}

output_file_csv = "./output.txt"
beer_data_set_csv = os.path.join("..", "Resources", "Data", "beers_joined.csv")

name_matches = []
beer_list = []

with open(output_file_csv, 'r') as o, open(beer_data_set_csv, 'r', encoding="utf8") as d:
    output = [x.strip() for x in o.readlines()]
    data_set = csv.reader(d)
    for row in data_set:
        beer_list.append(row[1])

for beer in output:
    if beer in beer_list:
        name_matches.append(beer)

beer_search_params["q"] = name_matches[1]
print(name_matches[0])
print(name_matches[1])
r = requests.get(url = untappd_url_beer_search, params = beer_search_params)
data = r.json()
beer_id = data["response"]["beers"]["items"][1]["beer"]["bid"]
# print(data["response"]["beers"]["items"][0]["beer"]["bid"])

beer_info_url = f"https://api.untappd.com/v4/beer/info/{beer_id}"
beer_info_params = {
    "client_id": untappd_id,
    "client_secret": untappd_secret
}

r = requests.get(url = beer_info_url, params = beer_info_params)
info = r.json()
print(output)
print(name_matches)
print(str(beer_id))
beer_info = info["response"]["beer"]
print(beer_info["beer_name"] + " has " + str(beer_info["rating_count"]) + " ratings and a score of " + str(beer_info["rating_score"]))