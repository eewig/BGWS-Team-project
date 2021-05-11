from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
	)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentCreateForm

# class PostListView(LoginRequiredMixin, ListView):
class PostHomeListView(ListView):
	model = Post
	template_name = 'home.html'
	login_url = 'login'


# class PostDetailView(LoginRequiredMixin, DetailView):
class PostDetailView(DetailView):
	model = Post
	form_class = CommentCreateForm
	template_name = 'post_detail.html'
	login_url = 'login'
	context_object_name = 'post'

	# def get(self, request, pk, *args, **kwargs):

	# 	post = get_object_or_404(self.model, id=pk)
	# 	comment_object = Comment()
	# 	form = self.form_class(instance=comment_object)
		
	# 	context = {'post':post, 'form':form}
	# 	return render(request, self.template_name, context)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.form_class
		return context


	def post(self, request, pk, *args, **kwargs):

		post = get_object_or_404(self.model, id=pk)
		comment_object = Comment(post=post, author=self.request.user)
		form = self.form_class(instance=comment_object, data=request.POST)

		if form.is_valid():
			form.save()
			return redirect('post_detail', pk=pk)

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
