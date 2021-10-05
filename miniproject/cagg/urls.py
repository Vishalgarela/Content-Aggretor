from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('history',views.history,name="History"),
    path('summaryy',views.summaryy,name="Summary")
]