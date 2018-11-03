from django import forms
from .models import Course

from django_select2.forms import ModelSelect2MultipleWidget, Select2Widget

class SearchForm(forms.Form):
	COURSES = map(lambda course: (course.department.name + course.number, course.title), Course.objects.all())
	searchbar = forms.ChoiceField(widget = Select2Widget, choices = COURSES)

	def clean_searchbar(self):
		data = self.cleaned_data['searchbar']
		print("data is: {}".format(data))
		return data