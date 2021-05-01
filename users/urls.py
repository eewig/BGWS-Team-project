from django.urls import path

from .views import SignUpView, UserProfileView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/<int:user_id>/', UserProfileView.as_view(), name='user_profile')
]