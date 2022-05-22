from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')


class Signin(View):
    def get(self, request):
        return render(request, 'homepage/signin.html')
    def post(self, request):
        tai_khoan = request.POST.get('username')
        mat_khau = request.POST.get("password")
        my_user = authenticate(username=tai_khoan, password=mat_khau)
        if my_user is None:
            return HttpResponse('User ko ton tai')
        return render(request, 'homepage/index.html')
class register(View):
    def get(self, request):
        return render(request, 'homepage/register.html')
class login(View):
    def get(self, request):
        return render(request, 'homepage/login.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'homepage/register.html', {'form': form})