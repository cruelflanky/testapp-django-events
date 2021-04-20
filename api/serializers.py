from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    #Making more human readable format
    date_of_event = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Event
        fields = ['name', 'date_of_event', 'price', 'city', 'tickets_left']