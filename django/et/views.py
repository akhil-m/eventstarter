from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from et.models import Event, EventForm

import datetime

def create_event(request):
	if request.method == 'POST':
		e = Event()
		e.name = request.POST.get('name', '')
		e.description = request.POST.get('description', '')
		e.goal = int(request.POST.get('goal', ''))
		day = int(request.POST.get('day', ''))
		month = int(request.POST.get('month', ''))
		year = int(request.POST.get('year', ''))
		e.deadline = datetime.datetime(year=year, month=month, day=day)
		e.save()
		return HttpResponseRedirect('/event/' + e.id + '/')

	return render_to_response('create_event.html', {}, context_instance=RequestContext(request))

def event_details(request, pk):
	try:
		e = Event.objects.get(pk=pk)
		return render_to_response('event.html', {'event': e}, context_instance=RequestContext(request))
	except Event.DoesNotExist:
		raise Http404

def form_test(request):
	return render_to_response('form_test.html', {}, context_instance=RequestContext(request))
