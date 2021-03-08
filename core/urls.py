from django.urls import path, include
from .views import index, product, contact

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contact'),
    path('produto/', product, name='product'),
]
