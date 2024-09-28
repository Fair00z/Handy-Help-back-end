from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
     path('', views.index,name='index'),
     path('how-it-works/', views.how_it_works,name='how-it-works'),
     path('about-us',views.about_us,name='about-us'),
     path('login/',views.login_page,name='login-page'),
     path('choice/',views.user_choice,name='user-choice'),
     path('worker_signup/',views.worker_signup,name='worker-signup'),
     path('logout/', views.logout_view, name='logout'),
     path('worker-home/', views.worker_home, name='worker-home'),
     path('worker-dashboard/', views.worker_dashboard, name='worker-dashboard'),
]
