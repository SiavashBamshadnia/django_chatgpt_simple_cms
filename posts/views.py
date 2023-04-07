from django.http import Http404
from django.shortcuts import render, get_object_or_404

from posts import models, filters


def home(request):
    """
    Retrieves a list of published posts and applies filters based on request parameters.
    It then renders the 'home.html' template with the filtered posts.
    """
    queryset = models.Post.objects.filter(status=models.Post.Status.PUBLISHED)
    filter = filters.PostFilter(request.GET, queryset=queryset)
    return render(request, 'home.html', {'filter': filter})


def post(request, post_id: id):
    """
    Retrieves a single post based on its ID.
    It checks if the current user is allowed to view the post, based on their permissions and the post's status.
    If the user is not allowed to view the post, an Http404 error is raised.
    If the user can view the post, it renders the 'post.html' template with the post and an optional message.
    """
    post = get_object_or_404(models.Post, pk=post_id)
    message = ''
    if request.user.is_superuser or request.user == post.author:
        if post.status == models.Post.Status.DRAFT:
            message = 'This post is a draft'
    else:
        if post.status != models.Post.Status.PUBLISHED:
            raise Http404
    return render(request, 'post.html', {'post': post, 'message': message})
