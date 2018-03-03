from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os
from django.conf import settings
import hashlib
import uuid
import json
from app.models import PROXY_users


@csrf_exempt
def proxy(request):
    session_cookie = request.COOKIES.get('dashboard.session')
    user_cookie = request.COOKIES.get('dashboard.user')
    session_token = ''
    if session_cookie is None or user_cookie is None:
        return HttpResponseRedirect(settings.HOST_URL + "login")
    try:
        query = PROXY_users.objects.get(username=user_cookie)
        session_token = query.session_token
    except Exception as e:
        return HttpResponseRedirect(settings.HOST_URL + "login")

    if session_cookie != session_token:
        return HttpResponseRedirect(settings.HOST_URL + "login")

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

@csrf_exempt
def login_post(request):
    if request.method != 'POST':
        returned = JsonResponse({'status': 'Invalid Request'}, status=403)
        returned['Access-Control-Allow-Origin'] = '*'
        return returned
    data = json.loads(request.body)
    username = data.get('username', '')
    password = data.get('password', '')
    try:
        query = PROXY_users.objects.get(username=username)
    except Exception as e:
        returned = JsonResponse({'status': 'Unauthorized'}, status=403)
        returned['Access-Control-Allow-Origin'] = '*'
        return returned
    id = query.id
    salt = query.salt
    pw = query.password
    hashed_password = str(hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest())
    if pw == hashed_password:
        session_token = uuid.uuid1()
        query.session_token = session_token
        query.save()
        response = HttpResponse(
            content=settings.HOST_URL + "#!/overview",
            status=302,
            content_type='document'
        )
        response['Location'] = settings.HOST_URL + "#!/overview"
        response.set_cookie('dashboard.session', session_token)
        response.set_cookie('dashboard.user', username) 
        return response
    else:
        final_array = dict()
        final_array['status'] = 'Unauthorized'
        returned = JsonResponse(final_array, status=403)
        returned['Access-Control-Allow-Origin'] = '*'
        return returned
