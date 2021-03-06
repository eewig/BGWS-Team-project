from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	
	class Meta(UserChangeForm.Meta):
		model = CustomUser
		fields = ('username', 'email', 'about', )

class CustomUserChangeForm(UserChangeForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email', 'about', )
