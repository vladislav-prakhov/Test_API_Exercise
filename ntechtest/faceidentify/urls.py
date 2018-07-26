from django.conf.urls import url
# from django.contrib import admin


from .views import (
    face_identify,
    face_identify_result
)

#from core import views as post_view
'''Django 1.10 no longer allows you to specify views as a string (e.g. 'myapp.views.home') in your URL patterns.'''

app_name = 'face_identify'

urlpatterns = [
    url(r'^$', face_identify, name='fi'),
    url(r'^result/$', face_identify_result, name='fi_result'),
]
