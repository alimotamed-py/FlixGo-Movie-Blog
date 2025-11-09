from django.views.generic import DetailView, ListView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category, Comment


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_details.html'
    context_object_name = 'post'
    slug_field = 'slug'       
    slug_url_kwarg = 'slug'   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.exclude(id=self.object.id).order_by('-created_at')[:4]
        context['comments'] = self.object.comments.filter(parent__isnull=True, active=True)
        context['photos'] = self.object.photos.all()

        return context

    
    
class CategoryPostView(ListView):
    model = Post
    template_name = 'post/post_category.html'
    context_object_name = 'posts'
    paginate_by = 1 

    def get_queryset(self):
       self.category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
       return Post.objects.filter(category__in=[self.category]).order_by('-created_at').prefetch_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
    
    
class CommentView(LoginRequiredMixin, View):
    login_url = 'login'            
    redirect_field_name = 'next'   

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get("text")
        parent_id = request.POST.get("parent_id")

        if content:
            Comment.objects.create(
                post=post,
                user=request.user,
                content=content,
                parent_id=parent_id if parent_id else None
            )

        return redirect("post:post_details", slug=post.slug)
    
    
class SearchView(ListView):
    model = Post
    template_name = 'post/search.html'
    context_object_name = 'results'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        if query:
            results = Post.objects.filter(title__icontains=query)
            if results.count() == 1:
                # اگر فقط یک نتیجه پیدا شد، ریدایرکت با slug
                post = results.first()
                return redirect('post:post_details', slug=post.slug)
            else:
                # اگر چند نتیجه پیدا شد، لیست رو نمایش بده
                return self.render_to_response({'results': results, 'query': query})
        else:
            # اگر ورودی خالی بود، می‌تونی برگردی به صفحه اصلی یا صفحه جستجو
            return redirect('home:home')
