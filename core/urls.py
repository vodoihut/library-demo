from django.urls import path
from .import views
from .views import HomeView, Signin, register, login



urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('sign/', Signin.as_view(), name='sign'),
    path('register/', views.register, name='register'),
    path('login/', login.as_view(), name='login')
]