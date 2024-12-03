from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_view(request, *args, **kwargs):
    data = {
        'nom': 'haroun',
        'profile': 'developpeur python'
    }
    return JsonResponse(data=data)