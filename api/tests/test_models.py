from django.test import TestCase
from django.utils import timezone
from api.models import Event, City

class EventModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        moscow = City.objects.create(name='Moscow')
        london = City.objects.create(name='London')
        event = Event.objects.create(
            name='Big party',
            date_of_event=timezone.now(),
            tickets_left=56
        )
        event.save()
        event.city.add(moscow, london)

    def test_price_for_today(self):
        event = Event.objects.get(id=1)
        price = event.price
        self.assertEquals(3000, price)
