from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('post/<int:id>',views.post_detail,name='post_detail'),
    path('login/',views.login_view,name='login'),
    path('register/',views.RegistrationView,name='register'),
    path('user/<int:id>/logout/',views.LogoutView,name='logout'),
    path('post/<int:id>/edit', views.edit_post, name='post_edit'),
    path('post/<int:id>/delete', views.delete_post, name='post_delete'),
]