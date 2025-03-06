from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth.models import User

class LoginView(View):

    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        print("GET")
        if request.user.is_authenticated:
            return redirect('emr:index') 
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('emr:index')  
        return render(request, self.template_name, {
            'form': form,
            'error': 'Invalid username or password'
        })

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
    

class AccountDetailView(View):
    model = User
    template_name = 'accounts/account_detail.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    

