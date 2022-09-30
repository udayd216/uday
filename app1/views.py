from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def app1_uday(request):
    return HttpResponse('<p>uday is good</p>')