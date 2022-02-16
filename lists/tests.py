from urllib import request
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')