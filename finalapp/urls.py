from django.urls import path
from . import views
urlpatterns = [
        # path('', views.demo,name='demo'),
        path('message',views.message,name='message'),
        path('form',views.form,name='form'),
        path('newpage',views.newpage,name='newpage'),
        path('',views.home,name='home'),

    ]