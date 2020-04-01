from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

subPages = [{"title": "Inicio", "url": "../home/"},
            {"title": "Album", "url": "../album/"}]


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


def split_columns(images, numcol):
    """ Splitthe list in images in columns """

    numrow = round((len(images) / numcol) + 0.5)

    img_col = [[] for i in range(numcol)]
    for i, j in zip(images, list(range(numcol))*numrow):
        img_col[j].append(i)

    return img_col


def gallery(request):
    types_choise = [choise[0] for choise in
            Image._meta.get_field('types').choices ]

    img_choise = [ Image.objects.all().filter(types=types)[0] 
            for types in types_choise]

    images = split_columns(img_choise, 3)

    return render(request, 
            'album/index.html', 
            {
                'images': images,
                'bskgrnd': "../../media/Edited_5196_BW.jpg",
                'subPages': subPages,
            })

def album(request, types='VA'):
    images = split_columns(Image.objects.all().filter(types=types), 3)

    return render(request, 
            'album/types.html', 
            {
                'images': images,
                'bskgrnd': "../../media/Edited_5196_BW.jpg",
                'subPages': subPages,
            })


def home(request):
    return render(request, 
            'home.html', 
            {
                'bskgrnd': "../../media/Edited_5196_BW.jpg",
                'subPages': subPages,
            })
