from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


from .forms import SearchForm
# Create your views here.

"""
-Have modal box popup for add course
-then when you find the course and click submit, it updates the database (stores the course)
-it also updates a list of courses currently selected (do this later)
-when you click "view schedules", it generates and displays the schedules
======
-same idea with adding a rule
"""
def index(request):
	"""
	form = SearchForm(request.POST)
	if request.method == 'POST':
		print("got post")
		if form.is_valid():
			print("valid data")
			print(form.cleaned_data['searchbar'])
	"""
	request.session['slot_count'] = 0
	request.session.save()
	return render(request, 'main/index2.html', {})

def add_slot(request):
	if ('slot_count' in request.session):
		request.session['slot_count'] += 1
	else:
		request.session['slot_count'] = 1
	request.session.save()
	print(request.session['slot_count'])
	return JsonResponse({'slot_id': request.session['slot_count']})

"""
press "edit slot"
form pops up
form is populated with courses already in that slot


press "edit slot"
javascript is passed the id of the slot you pressed
javascript adds a <li> element with the id to the slot_form_list (if it isn't already there)
javascript loads html into the element from the server
server uses get parameters to get slot id
server retrieves course data from session and renders it
server also renders form
"""
def render_slot_form(request):
	pass