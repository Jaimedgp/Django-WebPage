from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


# Create your views here.
def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(image = form.cleaned_data["image"],
                              name = form.cleaned_data["name"]
                              )
            new_image.save()
            return HttpResponseRedirect('/gallery/upload_image/')

def home(request):
    images_all = Image.objects.all()

    numCols = 3
    numRows = round((len(images_all) / numCols) + 0.5)

    images = [[] for i in range(numCols)]
    for i, j in zip(images_all, list(range(numCols))*numRows):
        images[j].append(i)

    subPages = [{"title": "Home", "url": "../home/"},]

    return render(request, 'home.html', {'images': images,
        'bskgrnd': "../../media/Edited_5196_BW.jpg",
        'subPages': subPages})
