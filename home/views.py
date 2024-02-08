from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Page from the theme 
    line_list = ['S1','S3']
    eqp_list = ['WSPDC1', 'WSPDC2']
    return render(request, 'pages/index.html',{'line_list' : line_list, 'eqp_list': eqp_list})

def bc_typography(request):
    return render(request, 'pages/bc_typography.html')
