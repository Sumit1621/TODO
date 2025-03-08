from django .urls import path
from .views import *

urlpatterns = [
    path('',home,name='home.html'), 
    path('update<pk>',update,name='update'),
    path('delete/<int:pk>/', views.delete_todo, name='delete'),
]
