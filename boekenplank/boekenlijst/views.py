from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book


# Create your views here.

def boekenlijst(request):
    
    template = loader.get_template('boekenlijst/boekenlijst.html')
    context = { 
        'boeken': Book.objects.all().values('title', 'author', 'description', 'language', 'cover_image')
    }

    return HttpResponse(template.render(context, request))