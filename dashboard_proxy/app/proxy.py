from django.http import JsonResponse
from django.http import HttpResponse
import requests


def proxy(request):
    path = request.get_full_path()
    requests_response = requests.get('http://kubernetes-dashboard.kube-system:443' + path)

    django_response = HttpResponse(
        content=requests_response.content,
        status=requests_response.status_code,
        content_type=requests_response.headers['Content-Type']
    )

    return JsonResponse({'status':'ok'}, status=200)
