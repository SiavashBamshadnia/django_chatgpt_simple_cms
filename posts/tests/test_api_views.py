from django.test import TestCase
from django.utils import lorem_ipsum


class TestApiViews(TestCase):
    def test_generate_title_from_content(self):
        response = self.client.post('/api/posts/generate_title_from_content/', {'content': 'test content'})

        self.assertEqual(response.status_code, 200)

    def test_generate_title_from_content_without_content(self):
        response1 = self.client.post('/api/posts/generate_title_from_content/')
        response2 = self.client.post('/api/posts/generate_title_from_content/', {'content': ''})
        response3 = self.client.post('/api/posts/generate_title_from_content/', {'content': '   '})

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 400)

    def test_generate_summary_from_content(self):
        content = '\n\n'.join(lorem_ipsum.paragraphs(3))
        response = self.client.post('/api/posts/generate_summary_from_content/', {'content': content})

        self.assertEqual(response.status_code, 200)

    def test_generate_summary_from_content_without_content(self):
        response1 = self.client.post('/api/posts/generate_summary_from_content/')
        response2 = self.client.post('/api/posts/generate_summary_from_content/', {'content': ''})
        response3 = self.client.post('/api/posts/generate_summary_from_content/', {'content': '   '})

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 400)

    def test_generate_content_from_title(self):
        response = self.client.post('/api/posts/generate_content_from_title/', {'title': 'django web framework'})

        self.assertEqual(response.status_code, 200)

    def test_generate_content_from_title_without_title(self):
        response1 = self.client.post('/api/posts/generate_content_from_title/')
        response2 = self.client.post('/api/posts/generate_content_from_title/', {'title': ''})
        response3 = self.client.post('/api/posts/generate_content_from_title/', {'title': '   '})

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 400)

    def test_generate_content_from_summary(self):
        summary = lorem_ipsum.paragraph()
        response = self.client.post('/api/posts/generate_content_from_summary/', {'summary': summary})

        self.assertEqual(response.status_code, 200)

    def test_generate_content_from_summary_without_title(self):
        response1 = self.client.post('/api/posts/generate_content_from_summary/')
        response2 = self.client.post('/api/posts/generate_content_from_summary/', {'summary': ''})
        response3 = self.client.post('/api/posts/generate_content_from_summary/', {'summary': '   '})

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response3.status_code, 400)
