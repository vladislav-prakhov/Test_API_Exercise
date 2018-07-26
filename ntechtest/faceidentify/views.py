from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import FaceIdentifyForm
from .models import FacePhoto
from django.conf import settings
from pprint import pprint
import requests


# Create your views here.
def face_identify(request):
    url = 'https://api.findface.pro/v1/identify'
    header = {'Authorization': 'TOK: m3MLGHi8SgbJOFQkC3-h-S2mpoajCRtO'}
    form = FaceIdentifyForm(request.POST or None, request.FILES)
    if form.is_valid():
        username_share = form['user_name'].value()
        # photo_share = request.FILES['photo']
        if form['threshold'].value() == '':
            threshold = 0
        else:
            threshold = form['threshold'].value()

        if form['res_n'].value() == '':
            res_n = 1
        else:
            res_n = form['res_n'].value()

        data = {
                'mf_selector': 'all',
                'threshold': threshold,
                'n': res_n,
        }

        instance = form.save()
        id = instance.pk
        print('\n\n')
        print(instance.pk)
        print(id)
        print('\n\n')
        print(instance.photo.path)
        # path = settings.BASE_DIR + 'media_cdn/None/' + instance.photo.filename()
        path = instance.photo.path
        print('\n\n')
        print(path)
        files = {
                'photo': open(path, 'rb')
        }
        request.session['username_share'] = username_share
        request.session['instance_pk'] = instance.pk
        # image = photo_share
        r = requests.post(url, headers=header, data=data, files=files)
        f = r.json()
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

        pprint(d)
        request.session['faces_data'] = d
        # return redirect("face_identify:fi_result", id=id)
        # return redirect("face_identify_result", id=id)
        return HttpResponseRedirect("result")
        # face_identify_result(request, id=id)
    context = {
        "form": form,
    }
    return render(request, "posts_form.html", context)


def face_identify_result(request):
    id = username_share = request.session.get('instance_pk')
    instance = get_object_or_404(FacePhoto, id=id)
    username_share = request.session.get('username_share')
    faces_data = request.session.get('faces_data')
    photo_share = instance.photo
    context = {
        "instance": instance,
        "photo": photo_share,
        "username": username_share,
        "faces_data": faces_data,
    }
    return render(request, "result.html", context)
