from django.urls import path
from .views import *
urlpatterns = [
    # path('test/', test, name='test'),
    path('', home, name="home"),
    path('<slug:category_slug>/', home, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', product_detail, name='product_detail'),
]