from django.shortcuts import render
from .forms import ImageModelForm
from .models import Image
import images


# Create your views here.
def upload_file_view(request):
    form= ImageModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ImageModelForm()
        #obj= Image.objects.get(activated=False)
        #with open(obj.file_name.path,'r') as f:
         #   reader = images.reader(f)


           # for i , row in enmerate(reader):
            #    if i==0:
             #       pass
              #  else:
               #     print(row)

    return render(request,'images/home.html',{'form':form})
