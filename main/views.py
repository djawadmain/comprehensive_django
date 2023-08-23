from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Post, Release, Comment
from django.core.cache import cache


# Create your views here.


class HelloView(View):
    def get(self, request):
        # new_release = Release(title='Hello Friends')
        # new_release.comments = [
        #     Comment(
        #         name='djawad',
        #         content='Hello bro'
        #     )
        # ]
        # new_release.save()

        get_cache = cache.get('hello_view')
        if get_cache:
            context = {
                'post': get_cache,
                'cache': True
            }
        else:
            context = {'posts': 'hello', 'cache': False}
            cache.set('hello_view', 'hello', timeout=25)

        return JsonResponse(context)


class IndexWebSocket(View):
    def get(self, request):
        return render(request, 'index.html')
