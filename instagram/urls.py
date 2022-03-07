from django.urls import URLPattern, path, include
from django.contrib.auth.decorators import login_required
from .views import (
    Home,
    PostListView
)
app_name = 'instagram'

urlpatterns =[
    path('', Home.as_view(), name= 'home'),
    path('profile', PostListView.as_view(), name = 'post_list'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]