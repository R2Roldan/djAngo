from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render


# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, 'blog_list.html', context)
