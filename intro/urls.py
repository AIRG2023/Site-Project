from django.urls import path
from pybo.views import base_views

app_name = 'intro'

urlpatterns = [
    path('', base_views.intro, name='index'),
]