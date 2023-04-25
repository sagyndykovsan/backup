from django.shortcuts import render
from event.models import Event, EventType
# Create your views here.

def index(request):
    events = Event.objects.all()
    return render(request, 'service.html', {'events': events})

