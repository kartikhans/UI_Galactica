# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST':
        list_of_paths = []

        print(request.FILES.getlist("file"))
        files = request.FILES.getlist("file")

        fs = FileSystemStorage()

        for i, img in enumerate(files):
            print(img)
            #with open('/home/galactica/Desktop/file_' + str(i), 'wb+') as destination:
            filename = fs.save("/home/galactica/Desktop/file_"+img.name, img)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)

        return render(request, 'home.html',{})
    return render(request, 'home.html')
