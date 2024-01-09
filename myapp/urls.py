from django.urls import path # import path from django.urls
from . import views # import views.py from the same directory


urlpatterns = [
	path('', views.home, name='home'),
 	path('home', views.home, name='home'),
 	path('contact', views.contact, name='contact'),
]