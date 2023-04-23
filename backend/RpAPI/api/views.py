from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def api_view(request, *args, **kwargs):
    print(request.body)
    data = json.loads(request.body)
    pre_data = json.dumps(data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post-data'] = dict(request.POST)
    print(request.headers)
    data['Content_type'] = request.content_type
    print(data)
    return JsonResponse(data)
