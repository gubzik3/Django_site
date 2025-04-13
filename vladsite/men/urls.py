from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('classno/', name_men),
    path('chetko/<int:menid>/', proverka),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]