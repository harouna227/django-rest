import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_view(request, *args, **kwargs):
    print(request.body) # retourne une chaine binaire
    data = json.loads(request.body) # traduit en json
    origin_data = json.dumps(data) # donnees d'origine
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post-data'] = dict(request.POST)
    print(request.headers)
    data['Conten_type'] = request.content_type
    return JsonResponse(data=data)