from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('topics_listing/',views.topics_listing,name='topics_listing'),
    path('contact/',views.contact,name='contact'),
    path('topics_detail/',views.topics_detail,name='topics_detail'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('login_view/',views.login_view,name='login_view'),
    path('register_view/',views.register_view,name='register_view'),
    path('profile/',views.profile,name='profile'),
    path('about_view/',views.about_view,name='about_view'),
    
]