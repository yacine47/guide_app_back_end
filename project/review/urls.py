
from django.urls import path
from . import views

urlpatterns = [
    path('get_reviews/',views.get_reviews,name='get_reviews'),
    path('delete_review/<int:id>/',views.delete_review,name='delete_review'),
]