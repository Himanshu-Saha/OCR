

# from django.shortcuts import render,redirect
# from .form import ImageForm
# from .models import Image
# # Create your views here.

# def index(request):
#     if request.method == "POST":
#         form=ImageForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance

#             return render(request,"main/index.html",{"obj":obj})
#     else:
#         form=ImageForm()
#     img=Image.objects.all()
#     return render(request,"main/index.html",{"img":img,"form":form})

import pytesseract
from PIL import Image
from django.shortcuts import render
from .form import ImageForm
from .models import Image as ImageModel

def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance

            return render(request, "main/index.html", {"obj": obj, "text": process(obj.image.path)})
    else:
        form = ImageForm()
    img = ImageModel.objects.all()
    return render(request, "main/index.html", {"img": img, "form": form})

def process(image_path):
    image =Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text