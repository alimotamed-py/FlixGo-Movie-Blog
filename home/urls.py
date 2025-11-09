from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name= 'home'),
    path("load-more-posts/", views.LoadMorePostsView.as_view(), name="load_more_posts"),
    
]

