from django.urls import path

from posts import api_views

urlpatterns = [
    path('generate_title_from_content/', api_views.generate_title_from_content, name='generate_title_from_content'),
    path('generate_summary_from_content/', api_views.generate_summary_from_content,
         name='generate_summary_from_content'),
    path('generate_content_from_title/', api_views.generate_content_from_title, name='generate_content_from_title'),
    path('generate_content_from_summary/', api_views.generate_content_from_summary, name='generate_content_from_summary'),
]
