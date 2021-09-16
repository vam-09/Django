from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="list"),
    path('update_task/<str:pk>',views.updateTask,name="update_task"),
    path('deletetask/<str:pk>',views.deleteTask,name="delete_task"),
    path('trial',views.trial,name = "trial"),
]


'''

python manage.py runserver

'''