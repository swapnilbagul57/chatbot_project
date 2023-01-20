import requests
from django.shortcuts import render
from django.http import HttpResponse, request
from model import response





def home(request):
    #input_data = request.GET.get("msg_input")
    #answer = response(input_data)
    return render(request, 'index.html')








