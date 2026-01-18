from django.urls import re_path as url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    
    url(r'^register/$',views.register,name="register"),
    url(r'^user_login/$',views.user_login,name='user_login'),
   
]