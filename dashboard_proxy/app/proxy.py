from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os


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
