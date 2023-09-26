from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')