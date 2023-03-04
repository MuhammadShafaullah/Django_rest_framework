

from django.urls import path
from .import views
urlpatterns = [
    
    path('data/<int:pk>',views.stuu,name='obj'),
    path('data',views.stu,name='obj'),
]
