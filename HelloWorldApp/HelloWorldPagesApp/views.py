from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('HelloWorldPages/index.html')
    context = {
        'name': "test",
    }
    return HttpResponse(template.render(context, request))

def hello(request, firstName):
    template = loader.get_template('HelloWorldPagesApp/index.html')
    context = {
        'name': firstName,
    }
    return HttpResponse(template.render(context, request))

def answer(request, firstName):
    answer = request.POST['answer']
    template = loader.get_template('HelloWorldPagesApp/answer.html')
    context = {
        'name': firstName,
        'answer': answer
    }
    return HttpResponse(template.render(context, request))
