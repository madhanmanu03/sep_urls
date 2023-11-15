from srh.views import *
from django.urls import path
app_name='onething'
urlpatterns=[
    path('kane/',kane,name='kane.html'),
]