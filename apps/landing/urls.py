from django.urls import path
from apps.landing.views import Index
from . import views 

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', views.user_login_view, name='user_login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    
]
