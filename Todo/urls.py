from django .urls import path
from .views import *

urlpatterns = [
    path('',home,name='home.html'), 
    path('update<pk>',update,name='update')
]
