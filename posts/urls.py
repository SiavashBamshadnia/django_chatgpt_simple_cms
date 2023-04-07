from django.urls import path

from posts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>', views.post, name='post'),
]
