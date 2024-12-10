from django.http import JsonResponse

from .models import Produit


# Create your views here.
def api(request):
    query = Produit.objects.all().order_by('?').first()
    data = {}
    
    if query:
        data['nom'] = query.nom
        data['description'] = query.description
        data['prix'] = query.prix
        
    return JsonResponse(data)