import re

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
	)
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import Post, Comment, Like, Tag
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentCreateForm


# class PostListView(LoginRequiredMixin, ListView):
class PostHomeListView(ListView):
	model = Post
	template_name = 'home.html'
	login_url = 'login'
	paginate_by = 5


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
		if not request.user.is_authenticated:
			return HttpResponseRedirect(reverse(self.login_url))

		post = get_object_or_404(self.model, id=pk)
		comment_object = Comment(post=post, author=self.request.user)
		form = self.form_class(instance=comment_object, data=request.POST)

		if form.is_valid():
			form.save()
			return redirect('post_detail', pk=pk)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ('title', 'body')
	template_name = 'post_edit.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		if form.is_valid():
			self.object = form.save()
			available_tags = [tag.name for tag in self.object.tags.all()]
			for tag_text in re.findall(r'#[^\r\n\t\f\v #]{1,30}', form.cleaned_data['body']):
				if tag_text in available_tags:
					available_tags.remove(tag_text)
				else:
					tag = Tag.objects.get_or_create(name=tag_text)[0]
					self.object.tags.add(tag)
			for tag_name in available_tags:
				self.object.tags.remove(Tag.objects.get(name=tag_name))
		return super().form_valid(form)

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
	fields = ('title', 'body')
	login_url = 'login'


	def form_valid(self, form):
		form.instance.author = self.request.user
		if form.is_valid():
			self.object = form.save()
			for tag_text in re.findall(r'#[^\r\n\t\f\v #]{1,30}', form.cleaned_data['body']):
				tag = Tag.objects.get_or_create(name=tag_text)[0]
				self.object.tags.add(tag)
		return super().form_valid(form)



class PostLikeView(View):
	login_url = 'login'

	def get(self, request, pk):
		if not request.user.is_authenticated:
			return HttpResponseRedirect(reverse(self.login_url))
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
			return JsonResponse({'likes': likes}, status=200)
		like.save()
		return JsonResponse({'ok': 'true'}, status=200)


class PostSearchView(ListView):
	template_name = 'post_search.html'
	login_url = 'post_search'
	context_object_name = 'posts'
	paginate_by = 10

	def get_queryset(self):
		search_request = self.request.GET['search']
		result = Post.objects.filter(
			Q(title__icontains=search_request) | Q(body__icontains=search_request)
			)
		return result


