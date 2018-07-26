import requests


pic = 'http://www.egorevista.es/var/ego/storage/images/reportajes/los-7-videoclips-mas-espantosos-de-la-historia/36591-3-esl-ES/los-7-videoclips-mas-espantosos-de-la-historia_gallery_a.jpg'
url = 'https://api.findface.pro/v1/identify'
url2 = 'https://api.findface.pro/v1/identify/?photo='
url3 = url2+pic
header = {'Authorization': 'TOK: m3MLGHi8SgbJOFQkC3-h-S2mpoajCRtO'}
data = {
        'photo': pic,
        'mf_selector': 'all',
        'threshold': 0.65,
        'n': 2,
}
r = requests.post(url2, headers=header, data=data)
data = r.json()
print(r)
print(data)
