import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse

class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='posts')
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Like')

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
	post = models.ForeignKey(
		Post,
		on_delete=models.CASCADE, 
		related_name='comments',)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)		
	comment = models.TextField(max_length=140)
	created_on = models.DateTimeField(auto_now_add=True)
	# active = models.BooleanField(default="True")

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('post_list')


class Like(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	liked = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.user.username} - {self.post.title} - {self.liked}'