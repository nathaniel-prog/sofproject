import json

with open('firstj_jason.json') as f:
    data= json.load(f) # convert json file to python

u = [{"hobbies":"boxe"}]


for element in data['person']:
    del element['username']

with open('new_first_jason.json', 'w') as f:
    json.dump(data , f) # dump method to convert python to json











