from django.views.generic import ListView
from django.http import JsonResponse
from django.template.loader import render_to_string
from post.models import Post
from django.views import View
from django.core.paginator import Paginator


class Home(ListView):
    model = Post
    template_name = "home/home.html"
    context_object_name = "posts"   
    paginate_by = 4    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["slider_posts"] = Post.objects.order_by("-created_at")[:4]
        return context




class LoadMorePostsView(View):
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get("page", 1))
        posts = Post.objects.all().order_by("-created_at")
        paginator = Paginator(posts, 4)  

        try:
            posts_page = paginator.page(page)
        except:
            posts_page = []

        html = render_to_string("includes/post_list.html", {"posts": posts_page})
        has_next = posts_page.has_next() if posts_page else False

        return JsonResponse({
            "html": html,
            "has_next": has_next
        })
        
        
