from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Content Aggregator"),
    path('history',views.history,name="History"),
    path('price',views.price,name="Price Comparision"),
]