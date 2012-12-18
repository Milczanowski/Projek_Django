from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



def index(request):	 		
	return render_to_response('index.html', {'title': 'Edytor - Strona Glowna'})

def nowy_pokoj(request):
	return render_to_response('room.html', {'title': 'Edytor - Strona Glowna'})

