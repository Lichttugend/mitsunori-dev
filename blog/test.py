from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Test content")

    def test_blog_list_status_code(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_status_code(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)