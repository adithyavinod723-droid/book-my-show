from django.urls import path

from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='home'),
    path('home/', views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add-movie/', views.add_movie, name='add_movie'),
]