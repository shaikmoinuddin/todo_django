from django.urls import path
from .views import addtask


urlpatterns = [
    path('addtask/', addtask, name='addtask'),
]
