from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def boekenlijst(request):
    
    template = loader.get_template('boekenlijst/boekenlijst.html')
    context = {
        'boeken': [
            {'titel': 'Walkaway', 'auteur': 'Cory Doctorow'},
            {'titel': 'Boek 2', 'auteur': 'Auteur 2'},
            {'titel': 'Boek 3', 'auteur': 'Auteur 3'},
        ],
    }
    return HttpResponse(template.render(context, request))