from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('post/<str:slug>/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    # CRUD PATHS
    path('create_post/', views.create, name='create_post'),
    path('update_post/<str:slug>/', views.update, name='update_post'),
    path('delete_post/<str:slug>/', views.delete, name='delete_post'),
    path('send_email/', views.sendEmail, name='send_email'),



]
