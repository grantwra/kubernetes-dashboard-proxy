from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os
from django.conf import settings


@csrf_exempt
def proxy(request):
    path = request.get_full_path()

    dashboard_response = requests.get(
    	'http://' + os.getenv(
    		'DASHBOARD_INTERNAL_ENDPOINT',
    		'kubernetes-dashboard.kube-system'
    		) + '.svc.cluster.local' + path
    	)

    response = HttpResponse(
        content=dashboard_response.content,
        status=dashboard_response.status_code,
        content_type=dashboard_response.headers['Content-Type']
    )

    return response


def login(request):
    response_content = ''
    for file in os.listdir(settings.STATIC_ROOT + 'app'):
        with open(settings.STATIC_ROOT + 'app/' + file, 'r') as content:
            for line in content:
                response_content += line

    response = HttpResponse(
        content=response_content,
        status=200,
        content_type='document'
    )
    return response
