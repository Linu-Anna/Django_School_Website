from django.urls import path
from . import views

urlpatterns = [
        path('register', views.register,name='register'),
        path('login',views.login,name='login'),
        path('logout',views.logout,name='logout'),
        # path('newpage',views.newpage,name='newpage'),
        # path('form',views.form,name='form'),
        # path('message',views.message,name='message')


    ]