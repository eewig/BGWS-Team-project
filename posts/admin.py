from django.contrib import admin

from .models import Post, Comment, Like

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 1
	# list_display = ('author', 'comment', 'post', 'created_on', 'active')
	# list_filter = ('active', 'created_on')
	# search_fields = ('author', 'comment')
	# actions = ['approve_comments', 'delete_comments']
	
	# def approve_comments(self, request, queryset):
	# 	queryset.update(active=True)

	# def delete_comments(self, request, queryset):
	# 	queryset.delete(author=self.model.author, post=self.model.post)

class PostAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
	]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)