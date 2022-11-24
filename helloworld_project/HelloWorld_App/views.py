# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('''{"Message": "Hello World!"}''', content_type="application/json")