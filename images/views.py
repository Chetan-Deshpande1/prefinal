from django.shortcuts import render
from .forms import ImageModelForm
from .models import Image
from collections import namedtuple 
#from PIL import Image
import csv
import os
import requests
import pdfplumber
import re
import parser
import pandas as pd



def upload_file_view(request):
    form= ImageModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ImageModelForm()
        #obj= Image.objects.get(activated=True)
        with pdfplumber.open(file_name.path) as pdf:
            #  page = pdf.pages[0]
            #  text = page.extract_text(x_tolerance=2)
            #  print(text)
           
            #  lines=text.split('\n')
            #  lines 
            #  line_one = re.compile(r'(fn_\d{7}) (image name) ([a-zA-Z]+ [a-z]+) ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
            #  for line in text.split('\n'):
            #     if line_one.match(line):
            #         print(line)
        
        

          
            # for  i ,row in enumerate(reader):
            #     if i==0:
            #         pass
            #     else:
            #         print(row)



           

    return render(request,'images/home.html',{'form':form})
