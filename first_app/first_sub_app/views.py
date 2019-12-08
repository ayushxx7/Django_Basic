from django.shortcuts import render
from django.http import HttpResponse #httpresponse
# Create your views here.

def home(request):
	return render(request, 'index.html',{'name':'Emiway, come out to play!'})

def index(request):
	return HttpResponse('Indexed Boy!')

def add(request):

	val1 = request.POST['number_one']
	val2 = request.POST['number_two']

	sum_val = int(val2)+int(val1)

	return render(request, 'result.html', {'result':sum_val})