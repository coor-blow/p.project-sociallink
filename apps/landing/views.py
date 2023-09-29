
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from apps.landing.forms import SignupForm
import logging
# Create your views here.

# logger = logging.getLogger(__name__)

# def user_login_view(request):
#     template_name = "account/login.html"
#     error_message = None

#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 logger.info(f"User '{username}' logged in successfully.")
#                 return redirect('landing/index.html')  # Use the correct URL pattern name
#             else:
#                 error_message = 'Sorry, something went wrong!'
#                 logger.warning(f"Failed login attempt for user '{username}'.")
#     else:
#         form = AuthenticationForm()

#     context = {'form': form, 'error_message': error_message}
#     return render(request, template_name, context)


def user_login_view(request):
    template_name = "account/login.html"
    error_message = None

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('landing:index')
            else:
                error_message = 'Sorry, something went wrong!'
    else:
        form = AuthenticationForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, template_name, context)



# def user_login_view(request):
#     template_name = "account/login.html"  # Assuming your template is in the "account" directory
#     error_message = None

#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(username)
#             user = authenticate(
#                 username=username,
#                 password=password,
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('landing/index.html')  
#             else:
#                 error_message = 'Sorry, something went wrong!'
#     else:
#         form = AuthenticationForm()

#     context = {'form': form, 'error_message': error_message}
#     return render(request, template_name, context)



def signup_view(request):
    template_name = "account/signup.html"
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('landing/index.html') 
    else:
        form = SignupForm()

    return render(request, template_name, {'form': form})
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')