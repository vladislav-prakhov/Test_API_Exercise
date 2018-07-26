import json
from pprint import pprint

with open('result.json') as f:
    data = json.load(f)

print(type(data))
# pprint(data)
for key, value in data['results'].items():  # faces can be multiple
    print(key)
    for info in value:
        # pprint(info)
        print('\n')
        pprint(info['confidence'])
        print(info['face']['meta'])
        ex_info = eval(info['face']['meta'])  # фамилия имя отчество
        print(ex_info['name'])
        print(info['face']['normalized'])  # face shortcut
        print(info['face']['thumbnail'])  # person photo
