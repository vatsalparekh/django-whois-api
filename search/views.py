import subprocess
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def serve(request, domain):

    try:
        result = subprocess.check_output(['whois', domain])
    except Exception:
        return Response('Error!!!')

    d = {}

    for items in result.splitlines():
        if items != '':
            try:
                d[items.split(':')[0]] = items.split(':')[1]
            except IndexError:
                d[items] = ''

    return HttpResponse(d)


@api_view(['GET'])
def search(request):

    domain = request.GET.get('domain', '')

    try:
        result = subprocess.check_output(['whois', domain])
    except Exception:
        return Response('Error!!!')

    d = {}

    for items in result.splitlines():
        if items != '':
            try:
                d[items.split(':')[0]] = items.split(':')[1]
            except IndexError:
                d[items] = ''

    return Response(d)
