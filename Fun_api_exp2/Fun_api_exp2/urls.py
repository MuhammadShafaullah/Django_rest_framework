
from django.contrib import admin
from django.urls import path
from fun_api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.hello),
]
