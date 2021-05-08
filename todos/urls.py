from django.urls import path
from . import views

urlpatterns = [
    path('insert_todo/',views.insert_todo_item, name='insert_todo_item'),
    path('list/', views.list_todo_items),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item, name='delete_todo_item'),

]
