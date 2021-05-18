from django.urls import path

from .views import (
	PostHomeListView,
	PostUpdateView,
	PostDetailView,
	PostDeleteView,
	PostCreateView,
	PostLikeView,
)

urlpatterns = [
	path('<pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
	path('detail/<pk>/', PostDetailView.as_view(), name='post_detail'),
	path('<pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('new/', PostCreateView.as_view(), name='post_new'),
	path('', PostHomeListView.as_view(), name='home'),
	path('like/<uuid:pk>/', PostLikeView.as_view(), name='post_like'),
]