from django.urls import path
from . import views


app_name = 'post'


urlpatterns = [
    path("details/<slug:slug>/", views.PostDetailView.as_view(), name="post_details"),
    path('category/<slug:slug>/', views.CategoryPostView.as_view(), name='post_category'),
    path("post/<int:post_id>/add-comment/", views.CommentView.as_view(), name="add_comment"),
    path("search/", views.SearchView.as_view(), name="search"),
]