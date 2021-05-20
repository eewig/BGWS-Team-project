from django.urls import path

from . import views

urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='user_profile'),
	path('update/', views.UserUpdateView.as_view(), name='user_update'),
	path('<int:pk>/posts/', views.UsersPostsListView.as_view(), name='user_posts'),
]