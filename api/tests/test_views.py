from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from api.views import EventDetail, EventList
from api.models import Event, City
from django.utils import timezone, dateparse

class EventViewTest(APITestCase):

    now = timezone.now()
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        moscow = City.objects.create(name='Moscow')
        london = City.objects.create(name='London')
        event = Event.objects.create(
            name='Big party',
            date_of_event=cls.now,
            tickets_left=14
        )
        event.save()
        event.city.add(moscow, london)

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_list(self):
        request = self.factory.get('/events/')
        response = EventList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_list_filter_city(self):
        request = self.factory.get('/events/?city=2')
        response = EventList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_list_filter_month(self):
        request = self.factory.get('/events/?month=4')
        response = EventList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_list_details(self):
        request = self.factory.post('/events/1', {'date_of_event': self.now}, format='json')
        response = EventDetail.as_view()(request, pk='1')
        self.assertEqual(response.status_code, 200)