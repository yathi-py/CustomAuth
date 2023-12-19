from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm, LoginForm


class SignupView(FormView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        creds = form.cleaned_data
        user = form.save(commit=False)
        user.set_password(creds['password'])
        user.save()
        login(self.request, user)
        if user:
            return HttpResponseRedirect(self.success_url)
        return super().form_valid(form)

class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        credentials = form.cleaned_data
        user = authenticate(
            username=credentials['email'], password=credentials['password'])
        if user:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials')
            return HttpResponseRedirect(reverse_lazy('accounts:login'))


def index(request):
    return render(request, 'registration/home.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('accounts:login'))

