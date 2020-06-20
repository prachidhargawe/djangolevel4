from AppL4 import views
from django.conf.urls import url
from django.urls import path

app_name = 'AppL4'

urlpatterns = [
    path('register/',views.register,name='registration'),
    path('user_login/',views.user_login,name='user_login')
]