from django.urls import path
from apps.landing.views import Index

app_name = 'land'

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
