from django.urls import path
from . import views

urlpatterns = [
    path('chal1/',views.chal1,name='1'),
    path('chal2/',views.chal2,name='2')
]
