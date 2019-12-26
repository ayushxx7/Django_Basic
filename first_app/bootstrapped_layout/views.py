from django.shortcuts import render
from . models import Destination
# Create your views here.

def home_bootstrap(request):

	# dest_one = Destination()
	# dest_one.name = 'Delhi'
	# dest_one.price = '$400'
	# dest_one.desc = 'Delhi se hu bc!!'
	# dest_one.img = 'destination_1.jpg'

	# dest_two = Destination()
	# dest_three = Destination()
	
	# dest_two.name = 'No offers!'
	# dest_two.price = '$400'
	# dest_two.desc = 'Delhi se hu bc!!'
	# dest_two.img = 'destination_1.jpg'

	destination_list = reversed(Destination.objects.all())
	return render(request,'index.html',{'destination_list':destination_list})