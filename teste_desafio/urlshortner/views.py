from queue import Empty
from tkinter import N
from unicodedata import name
from django.shortcuts import render, redirect

import random
from .models import Url
import string
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def createshorturl(request):
    if request.method == 'POST':
        slug = ''.join(random.choice(string.ascii_letters)
                       for x in range(10))
        url = request.POST["url"]
        if url != "":
            new_url = Url(url=url, slug=slug)
            new_url.save()
            messages.info(
                request, ('New URL is :' + '  localhost:8000/' + new_url.slug))
        else:
            messages.info(
                request, ('Url fiel is empty, please paste the link that you want to short'))
        return redirect('/')


def urlcreated(request):
    url = Url.objects.all()
    return render(request, 'urls.html', {'url': url})


def shortredirect(request, term):
    try:
        link = Url.objects.get(slug=term)
        return redirect(link.url)
    except Url.DoesNotExist:
        return redirect('/')
