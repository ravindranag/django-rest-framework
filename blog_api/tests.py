from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


# Create your tests here.
class PostTest(APITestCase):
    
    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def create_post(self):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username='testuser1', password='123456789')
        data = {
            'title': 'new',
            'author': '1',
            'excerpt': 'new',
            'content': 'new'
        }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')