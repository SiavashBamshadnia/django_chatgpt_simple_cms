from django.test import TestCase
from django.urls import resolve

from posts import api_views


class TestApiUrls(TestCase):
    def test_generate_title_from_content_api_url(self):
        url = '/api/posts/generate_title_from_content/'

        self.assertEqual(resolve(url).func, api_views.generate_title_from_content)

    def test_generate_summary_from_content(self):
        url = '/api/posts/generate_summary_from_content/'

        self.assertEqual(resolve(url).func, api_views.generate_summary_from_content)

    def test_generate_content_from_title(self):
        url = '/api/posts/generate_content_from_title/'

        self.assertEqual(resolve(url).func, api_views.generate_content_from_title)

    def test_generate_content_from_summary(self):
        url = '/api/posts/generate_content_from_summary/'

        self.assertEqual(resolve(url).func, api_views.generate_content_from_summary)
