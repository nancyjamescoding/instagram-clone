from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from .models import Post
from django.views.generic import(
    ListView
)

# Create your views here.
class PostListView(ListView):
    template_name = 'instagram/profile.html'
    queryset= Post.objects.all()
    context_object_name = 'posts'

    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Lamding page view
def home(request):
    if request.user.is_authenticated:
            # If a user is logged in, redirect them to a page informing them of such
        return redirect('/profile')
    else:
        return render(request, 'instagram/home.html')
