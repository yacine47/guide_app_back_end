
from django.urls import path
from . import views

urlpatterns = [
    path('get_reviews/',views.get_reviews,name='get_reviews'),
]