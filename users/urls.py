from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
	path('signup/', views.SignupView, name='signup'),
	path('login/', views.LoginView, name='login'),
	path('logout/', views.LogoutView, name='logout'),
]
