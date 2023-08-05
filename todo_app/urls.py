from django.urls import path
from .views import addtask, mark_as_done, mark_as_undone, edit, delete_task


urlpatterns = [
    # adding a task
    path('addtask/', addtask, name='addtask'),
    # mark as done task
    path('mark_as_done/<int:pk>/', mark_as_done, name='mark_as_done'),
    # mark as undone task
    path('mark_as_undone/<int:pk>/', mark_as_undone, name='mark_as_undone'),
    # edit task
    path('edit/<int:pk>/', edit, name='edit'),
    # delete task
    path('delete/<int:pk>/', delete_task, name='delete'),

]
