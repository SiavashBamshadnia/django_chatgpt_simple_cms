import markdown as md
from django.contrib.auth.models import User
from django.test import TestCase

from posts import models


class TestViews(TestCase):
    def setUp(self):
        self.author1 = User.objects.create_user(username='author 1', password='author 1')
        self.author2 = User.objects.create_user(username='author 2', password='author 2', is_staff=True)
        self.post1 = models.Post.objects.create(title='test title 1', summary='test summary 1',
                                                content='test content 1', status=models.Post.Status.PUBLISHED,
                                                author=self.author1)
        self.post2 = models.Post.objects.create(title='test title 2', summary='test summary 2',
                                                content='test content 2', status=models.Post.Status.PUBLISHED,
                                                author=self.author1)
        self.post3 = models.Post.objects.create(title='test title 3', summary='test summary 3',
                                                content='test content 3', status=models.Post.Status.DRAFT,
                                                author=self.author2)
        self.post4 = models.Post.objects.create(title='test title 4', summary='test summary 4',
                                                content='test content 4', status=models.Post.Status.PUBLISHED,
                                                author=self.author2)

    def test_home_page(self):
        response = self.client.get('/posts/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, '<h1>Home</h1>')
        self.assertContains(response, '<h2><a href="/posts/1" target="_blank">Test Title 1</a></h2>')
        self.assertContains(response, '<h2><a href="/posts/2" target="_blank">Test Title 2</a></h2>')
        self.assertNotContains(response, '<h2><a href="/posts/3" target="_blank">Test Title 3</a></h2>')
        self.assertContains(response, '<h2><a href="/posts/4" target="_blank">Test Title 4</a></h2>')

    def test_home_page_with_author_filter(self):
        response = self.client.get('/posts/?author=1')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, '<h1>Home</h1>')
        self.assertContains(response, '<h2><a href="/posts/1" target="_blank">Test Title 1</a></h2>')
        self.assertContains(response, '<h2><a href="/posts/2" target="_blank">Test Title 2</a></h2>')
        self.assertNotContains(response, '<h2><a href="/posts/3" target="_blank">Test Title 3</a></h2>')
        self.assertNotContains(response, '<h2><a href="/posts/4" target="_blank">Test Title 4</a></h2>')

    def test_post_page_with_published_post(self):
        response = self.client.get(f'/posts/1')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')
        self.assertContains(response, '<h1>Test Title 1</h1>')

    def test_post_with_markdown(self):
        response = self.client.get(f'/posts/1')
        html = md.markdown(self.post1.content)

        self.assertContains(response, html)

    def test_unpublished_post_page(self):
        response = self.client.get(f'/posts/3')

        self.assertEqual(response.status_code, 404)

    def test_unpublished_post_page_with_writer_user(self):
        self.client.login(username='author 2', password='author 2')
        response = self.client.get(f'/posts/3')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This post is a draft')

    def test_unpublished_post_page_with_super_user(self):
        User.objects.create_superuser(username='admin', password='admin')
        self.client.login(username='admin', password='admin')
        response = self.client.get(f'/posts/3')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This post is a draft')

    def test_unpublished_post_page_with_other_user(self):
        self.client.login(username='author 1', password='author 1')
        response = self.client.get(f'/posts/3')

        self.assertEqual(response.status_code, 404)

    def test_post_page_without_post(self):
        response = self.client.get(f'/posts/99')

        self.assertEqual(response.status_code, 404)
