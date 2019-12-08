from django.urls import path
from . import views

urlpatterns = [
	path('bs',views.home_bootstrap,name='bootstrap')
]