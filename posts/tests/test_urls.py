from django.test import TestCase
from django.urls import resolve

from posts import views


class TestUrls(TestCase):
    def test_home_url(self):
        url = '/posts/'

        self.assertEqual(resolve(url).func, views.home)

    def test_post_url(self):
        url = '/posts/1'

        self.assertEqual(resolve(url).func, views.post)
