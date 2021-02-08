from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.template.loader import get_template


def home_page(request):
    if request.method == 'GET':
        rendered_template = render(request, template_name='home.html')

        return HttpResponse(rendered_template)
    else:
        raise Http404
