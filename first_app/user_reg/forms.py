from django import forms

class UserForm(forms.ModelForm):

	class Meta:

		model = user
		widgets = {
		'password': forms.PasswordInput()
		}