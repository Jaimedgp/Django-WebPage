from django.urls import path
from . import views


app_name = 'gallery'
urlpatterns = [
        path("home/", views.home, name='home'),

        path("album/", views.gallery),
        path("album/types='VA'", views.album, {'types': 'VA'}),
        path("album/types='AT'", views.album, {'types': 'AT'}),
        path("album/types='PA'", views.album, {'types': 'PA'}),
]
