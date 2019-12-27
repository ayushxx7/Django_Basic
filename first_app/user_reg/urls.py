from django.urls import path
from . import views # importing views

urlpatterns = [
	path('register',views.register,name='register_form'),
	path('login',views.login,name='login'),
	path('logout',views.logout,name='logout')
]