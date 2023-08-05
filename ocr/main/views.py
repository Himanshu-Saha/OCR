import pytesseract
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from .form import ImageForm
from .models import Image as ImageModel
from django.http import HttpResponse
import json

def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            return render(request, "main/index.html")
    else:
        form = ImageForm()
    img = ImageModel.objects.all()
    return render(request, "main/index.html", {"img": img, "form": form})

def process(request):
    image_path = ""
    image_url = ""
    obj = None
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            image_path = obj.image.path
            image_url = obj.image.url
    image =Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    response_data = {"extracted_text": extracted_text,"path":image_url}
    return JsonResponse(response_data)