from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BlogListView


app_name = "blog"
urlpatterns = [
    path('', BlogListView.as_view(), name="home")
]