from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views import View 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


class UserProfileView(View):
	def get(self, request, user_id):
		user = CustomUser.objects.get(pk=user_id)
		return render(request, 'users/user_profile.html', {'this_user': user})


class UserUpdateView(LoginRequiredMixin, UpdateView):
	model = CustomUser
	fields = ['username', 'email', 'about', 'pic']
	template_name = 'users/user_update.html'

	def get_success_url(self):
		return reverse('user_profile', kwargs={'user_id': self.request.user.id})

	def get_object(self):
		return self.request.user


class UsersPostsListView(LoginRequiredMixin, DetailView):
	model = CustomUser
	context_object_name = 'this_user'
	template_name = 'users/user_posts.html'
	# paginate_by = 5

	# def get_context_data(self, pk, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['page_obj'] = Paginator(object.posts.all(), per_page=self.paginate_by)


