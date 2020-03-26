from django.urls import path, include

from . import views

app_name = 'home'
urlpatterns = [
	path('', views.HomeView, name='home'),
	path('account/profile/', views.AccountView, name='profile'),
	path('account/personalinfo/save/', views.PersonalInfoSaveView, name='personalinfo_save'),
	path('account/avatar/save/', views.AvatarSaveView, name='avatar_save'),
]
