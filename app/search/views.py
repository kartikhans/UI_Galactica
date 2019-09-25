# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from app.settings import BASE_DIR

from process import Processor

def generate_media_url():
    # create directory for current timestamp
    timestr = time.strftime("%Y%m%d-%H%M%S")
    media_path = os.path.join(BASE_DIR,"media")
    if not os.path.exists(media_path):
        os.mkdir(media_path);

    os.mkdir(os.path.join(media_path,timestr))
    media_path_timestamp = os.path.join(media_path,timestr)

    return media_path_timestamp;

def home(request):

    if request.method == 'POST':
        list_of_paths = []
        media_path = generate_media_url()
        processor = Processor(media_path)

        print("Files uploaded", request.FILES.getlist("file"))
        files = request.FILES.getlist("file")

        fs = FileSystemStorage()

        for i, img in enumerate(files):
            print(img)
            filename = fs.save(os.path.join(media_path,img.name), img)
            uploaded_file_url = fs.url(filename)
            print("file uploaded to : ", uploaded_file_url)

        processor.run();

        return render(request, 'home.html',{})
    return render(request, 'home.html')
