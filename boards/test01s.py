from django.test import TestCase
# from django.urls import reverse
from django.urls import reverse
from django.urls import resolve
from .models import Board
from .views import board_topics
from .views import new_topic

# Create your tests here.
# class HomeTest(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEquals(view.func, home)

# class BoardTopicsTests(TestCase):
    # def setUp(self):
    #     Board.objects.create(name='Django', description='Django board.')
    
    # def test_board_topics_view_success_status_code(self):
    #     url = reverse('board_topics', kwargs={'pk':1})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_board_topics_view_not_found_status_code(self):
    #     url = reverse('board_topics', kwargs={'pk':99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)

    # def test_board_topics_url_resolves_board_topics_view(self):
    #     view = resolve('/boards/1/')
    #     self.assertEquals(view.func, board_topics)

class NewTopicTest(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
    
    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    # def test_new_topic_view_not_found_status_code(self):
    #     url = reverse('new_topic', kwargs={'pk':100})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)
    
    # def test_new_topic_url_resolves_new_topic_view(self):
    #     view = resolve('/boards/1/new/')
    #     self.assertEquals(view.func, new_topic)