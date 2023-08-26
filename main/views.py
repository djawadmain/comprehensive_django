from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Post, Release, Comment
from django.core.cache import cache
from django.utils.safestring import mark_safe
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


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


class JoinChat(View):
    def get(self, request, username):
        return render(request, 'join_chat.html', {'username_json': mark_safe(json.dumps(username))})


class NewMessage(View):
    def get(self, request, username):
        try:
            text = request.GET['text']
            to_user = request.GET['to']

            channel_layer = get_channel_layer()
            group_name = f'chat_{to_user}'

            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type': 'chat_message',
                    'message': {'sender': username, 'receiver': to_user, 'message': text}
                }
            )

            success = True
        except None:
            success = False

        return JsonResponse({
            'success': success
        })
