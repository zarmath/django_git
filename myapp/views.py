from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from.models import PersonItem



# Create your views here.
def home(request):
	Personas = PersonItem.objects.all()
	return render(request, 'home_myapp.html',{"personas": Personas})