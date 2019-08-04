
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
  
def index(request):
	#return HttpResponse("<!DOCTYPE html><html><h1>OLLLAA</h1</html>")
	return render(request, '../templates/index.html')
