from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post
from django.views.generic import(
    ListView, TemplateView
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
class Home(TemplateView):
    template_name = 'instagram/home.html'