import requests
from pprint import pprint
import json

url = 'https://api.findface.pro/v1/identify'
header = {'Authorization': 'TOK: m3MLGHi8SgbJOFQkC3-h-S2mpoajCRtO'}
data = {
        'mf_selector': 'all',
        'threshold': 0.65,
        'n': 2,
}
files = {
        'photo': open('/mnt/c/linux_transfer_folder/Coding/ntechlab_test/pics/steklovata.jpg', 'rb')
}

r = requests.post(url, headers=header, data=data, files=files)
f = r.json()

print(r)
pprint(f)
d = {}
for key, value in f['results'].items():  # faces can be multiple
    print(key)
    d[key] = {}
    face_num = 0
    for info in value:
        # pprint(info)
        face_num += 1
        face_name = 'face_ex_' + str(face_num)
        d[key].update({face_name: {}})
        print('\n')
        pprint(info['confidence'])
        d[key][face_name].update({'confidence': info['confidence']})
        print(info['face']['meta'])
        ex_info = eval(info['face']['meta'])  # фамилия имя отчество
        print(ex_info['name'])
        d[key][face_name].update({'name': ex_info['name']})
        print(info['face']['normalized'])  # face shortcut
        d[key][face_name].update({'normalized_url': info['face']['normalized']})
        print(info['face']['thumbnail'])  # person photo
        d[key][face_name].update({'thumbnail_url': info['face']['thumbnail']})
        print('\n\n')

print('\n')
pprint(d)
