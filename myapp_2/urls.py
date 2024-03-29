from django.urls import path
from myapp_2.views import name

urlpatterns = [
    path(f'website/<str:names>',name)

]