from django.shortcuts import render
from django.http import HttpResponse
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
	form = SearchForm(request.POST)
	if request.method == 'POST':
		print("got post")
		if form.is_valid():
			print("valid data")
			print(form.cleaned_data['searchbar'])

	return render(request, 'main/index.html', {"form": form})