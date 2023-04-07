from django_filters import FilterSet

from posts import models


class PostFilter(FilterSet):
    class Meta:
        model = models.Post
        fields = ['author']
