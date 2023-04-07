from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from posts import models, forms


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'colored_status', 'created_at', 'link']
    list_display_links = list_display[0:-1]
    date_hierarchy = 'created_at'
    search_fields = ['title', 'summary', 'content']
    form = forms.PostForm
    exclude = ['author']

    # Overriding the get_queryset method to filter the Post queryset based on the current user
    def get_queryset(self, request):
        super_call = super().get_queryset(request)
        # All posts are shown to superusers
        if request.user.is_superuser:
            return super_call
        # Only posts created by the current user are shown to non-superusers
        return super_call.filter(author=request.user)

    @admin.display(description='status', ordering='status')
    def colored_status(self, obj: models.Post):
        if obj.status == models.Post.Status.PUBLISHED:
            color = 'auto'
        else:  # if obj.status == models.Post.Status.DRAFT:
            color = 'blue'
        return mark_safe(f'<span style="color: {color}">{obj.get_status_display().capitalize()}</span>')

    @admin.display(description='link')
    def link(self, obj: models.Post):
        return mark_safe(f'<a href="{reverse("post", kwargs={"post_id": obj.id})}" target="_blank">Link</a>')

    # Set post author as current user if post is new
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if not obj:  # create
            return []
        return ['created_at', 'updated_at']

    def get_list_filter(self, request):
        list_filter = ['status', 'created_at', 'updated_at']
        if request.user.is_superuser:
            list_filter.append('author')
        return list_filter
