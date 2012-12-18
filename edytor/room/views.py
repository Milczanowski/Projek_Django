from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request, room_id): 		 		
	try:		
		button = request.GET.get('button')
	except Exception, e:
		return render_to_response('room.html', {'room_id': room_id, 'file_name': "as"})		
	else:
		return render_to_response('room.html', {'room_id': room_id, 'file_name': button})