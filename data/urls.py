from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import admin_login


urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('signup/', views.signup, name='signup'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
