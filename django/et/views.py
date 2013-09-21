from django.shortcuts import render_to_response
from django.http import HttpResponse
from et.models import Event, EventForm

def create_event(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/thanks/')
	else:
		form = EventForm()

	return render_to_response('create_event.html', {'EventForm': form})

def thanks(request):
	return HttpResponse('Thanks for creating an event')
