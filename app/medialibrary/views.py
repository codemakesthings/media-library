# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(b"The Media Library is currently under maintenance. Please come back soon.")
