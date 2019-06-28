'''
TODO:
- Mock API reponse so you can continue testing --> reached API limit
- Print out the exact matches and stats for each match: {name}, {type}, {number of ratings}, {rating}
- BUG: searching "Budweiser" yields "Bud Light" as first result and "Budweiser" second.
       figure out a way to search for exact matc

- Make a simple search that allows user to enter in which type of beer they want and you are returned the top rated beer for that type.
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
beer_info_params = {
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

beer_stats = open("beers_stats.txt", "a+")

for beer in name_matches:
    try:
        beer_search_params["q"] = beer
        r = requests.get(url = untappd_url_beer_search, params = beer_search_params)
        data = r.json()
        print(data)
        beer_id = data["response"]["beers"]["items"][1]["beer"]["bid"]
        beer_info_url = f"https://api.untappd.com/v4/beer/info/{beer_id}"
        r = requests.get(url = beer_info_url, params = beer_info_params)
        info = r.json()
        beer_info = info["response"]["beer"]
        info_string = beer_info["beer_name"] + " is a " + str(beer_info["beer_style"]) + " beer. It has " + str(beer_info["rating_count"]) + " ratings and a score of " + str(beer_info["rating_score"]) + "."
        beer_stats.write(info_string + "\n")
    except Exception as e:
        print(e)

beer_stats.close()