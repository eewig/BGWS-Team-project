from django.urls import path

from . import views

urlpatterns = [
	path('<pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
	path('detail/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
	path('<pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
	path('new/', views.PostCreateView.as_view(), name='post_new'),
	path('', views.PostHomeListView.as_view(), name='home'),
	path('like/<uuid:pk>/', views.PostLikeView.as_view(), name='post_like'),
	path('search/', views.PostSearchView.as_view(), name='post_search')
]