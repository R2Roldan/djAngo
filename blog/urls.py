from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BlogDeletView, BlogListView,BlogCreateView, BlogDetailView, BlogUpdateView,DeleteView


app_name = "blog"
urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/',BlogCreateView.as_view(), name='create'),
    path('<int:pk>/',BlogDetailView.as_view(),name="detail"),
    path('<int:pk>/update/',BlogUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',BlogDeletView.as_view(),name="delete"),
]