from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('test/', test),
    path('<slug:category_slug>/', home, name='products_by_category')
]