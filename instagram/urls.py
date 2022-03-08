from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from .views import (
    home,
    PostListView,
)
app_name = 'instagram'

urlpatterns =[
    path('', home, name= 'home'),
    path('profile', PostListView.as_view(), name = 'post_list'),
    path('accounts/register/', RegistrationView.as_view(success_url='/profile'), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout')
]