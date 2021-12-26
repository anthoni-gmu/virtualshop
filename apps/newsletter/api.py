from django.http import JsonResponse
from .models import Subscriber
import json

def api_add_subscriber(request):
    data=json.loads(request.body)
    email=str(data['email'])
    s=Subscriber.objects.create(email=email)
    return JsonResponse({'success': True})