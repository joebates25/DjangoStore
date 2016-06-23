from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def index(request):
    user = authenticate(username='joseph', password='cabrini93')
    return HttpResponse("Hello World")