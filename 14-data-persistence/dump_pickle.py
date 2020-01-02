#!/usr/bin/env python3

import pickle

data = {
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
}


with open('data.txt', 'wb') as outfile:
    pickle.dump(data, outfile)


with open('data.txt', 'rb') as infile:
    data2 = pickle.load(infile)

print(data2)
