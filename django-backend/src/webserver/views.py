from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_req(request):
    return HttpResponse("<h1>test msg</h1>")
