from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request=request,
                  template_name="main/index.html")