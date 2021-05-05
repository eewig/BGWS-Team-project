import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		related_name='posts')
	likes = models.ManyToManyField(get_user_model(), through='Like')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
	post = models.ForeignKey(
		Post, 
		on_delete=models.CASCADE, 
		related_name='comments',)
	comment = models.CharField(max_length=140)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('post_list')


class Like(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	liked = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.user.username} - {self.post.title} - {self.liked}'