from django.shortcuts import render
from . import gen
from PIL import Image
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def generate(request):
    a = request.GET['idea']
    print(a)
    gen.Gen(a)

def display_image(request):
    generate(request)
    image = Image.open("APP/static/1.png")
    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG")
    return response