from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
	)
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Post, Like


# class PostListView(LoginRequiredMixin, ListView):
class PostHomeListView(ListView):
	model = Post
	template_name = 'home.html'
	login_url = 'login'
	paginate_by = 5


# class PostDetailView(LoginRequiredMixin, DetailView):
class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
	login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ('title', 'body',)
	template_name = 'post_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ('title', 'body',)
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostLikeView(LoginRequiredMixin, View):
	login_url = 'login'

	def get(self, request, pk):
		try:
			p = Post.objects.get(id=pk)
		except ObjectDoesNotExist:
			return JsonResponse({'error': 'Not found.'})
		like = Like.objects.get_or_create(user=self.request.user, post=p)[0]
		print(like)
		if self.request.GET.get('like') == 'false':
			like.liked = False
		elif self.request.GET.get('like') == 'true':
			like.liked = True
		else:
			likes = Like.objects.filter(post=p, liked=True).count()
			return JsonResponse({'likes': likes})
		like.save()
		return JsonResponse({'ok': 'true'})





