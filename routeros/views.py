from django.shortcuts import render
from django.http import HttpResponse
import routeros_api

connection = routeros_api.RouterOsApiPool('192.168.53.253', username='api-admin', password='LOgh943fgh8t7', plaintext_login=True)
api = connection.get_api()
ppp_secrets=api.get_resource('/ppp/secret')



def index(request):
    return HttpResponse(ppp_secrets.get())
