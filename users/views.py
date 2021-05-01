from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View 
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


class UserProfileView(View):
	def get(self, request, user_id):
		user = CustomUser.objects.get(pk=user_id)
		return render(request, 'users/user_profile.html', {'user': user})
