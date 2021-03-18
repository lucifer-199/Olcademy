from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('queries',views.queries,name="queries"),
    path('signup',views.handleSignup,name="handleSignup"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout',views.handleLogout,name="handleLogout"),
]
