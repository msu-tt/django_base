from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    # return HttpResponse('ok')
    context = {
        'name':'9.9ri'
    }
    return render(request,'book0/index.html',context=context)