from django.urls import path
from . import views # importing views

urlpatterns = [
	path('',views.home, name = 'home'),
	path('index',views.index, name = 'index'),
	path('add',views.add, name = 'result')

]
