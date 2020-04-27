from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),
    path('current/', views.currenttodos, name="currenttodos"),
    path('create/', views.createtodo, name="createtodo"),
    path('todo/<int:todo_pk>/', views.viewtodo, name="viewtodo"),



]
