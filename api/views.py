from django.http import Http404, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from datetime import date

# Create your views here.

#There are all possibilities of API
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Events list':'events/',
        'Events detail':'events/<int:pk>/',
        'Events filter by city':'events/?city=int',
        'Events filter by month':'events/?month=int',
        }

    return Response(api_urls)


#Main class for handling /events/ with filters
class EventList(APIView):

    #Filtering by city
    def get_object_by_city(self, city):
        try:
            return Event.objects.filter(city=city)
        except Event.DoesNotExist:
            raise Http404

    #Filtering by month
    def get_object_by_month(self, month):
        try:
            return Event.objects.filter(date_of_event__month=month)
        except Event.DoesNotExist:
            raise Http404

    #The list of all events
    def get_object_list(self):
        try:
            return Event.objects.all()
        except Event.DoesNotExist:
            raise Http404

    #GET request handler for /events/
    def get(self, request, format = None):
        city = request.GET.get('city')
        month = request.GET.get('month')
        if city:
            event = self.get_object_by_city(city)
        elif month:
            event = self.get_object_by_month(int(month))
        else:
            event = self.get_object_list()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

class EventDetail(APIView):

    #POST request handler for specific item
    def post(self, request, pk, format = None):
        try:
            date = request.data['date_of_event']
            event = Event.objects.get(pk=pk, date_of_event=date)
            if event.tickets_left == 0:
                return Response('No tickets left')
            event.tickets_left -= 1 #Everytime we call this func, we make our API to minus 1 place of event
            event.save()
            return HttpResponse('')

        except Event.DoesNotExist:
            return Response('Wrong time of event')