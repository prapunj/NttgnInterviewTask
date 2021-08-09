from django.urls import path,re_path
from .views import interfaces,interface_detail

urlpatterns = [
    path('interfaces', interfaces, name='interfaces'),
    path(r'interface/<str:interface>/<str:option>', interface_detail),
]