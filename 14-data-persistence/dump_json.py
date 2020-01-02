#!/usr/bin/env python3

import json

data = {
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
}

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('data.txt', 'rb') as infile:
    data2 = json.load(infile)

print(data2)
