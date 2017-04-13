from django.shortcuts import render

from django.http import HttpResponse

from sunflower.models import Flower


def hi(request):
    return HttpResponse("You said hi I said bye")

def index(r):
    return render(r, "sunflower/index.html")


def flower_crud(request):
    if request.method == "GET":
        return render(request, 'sunflower/flower_form.html')
    else:  # assumes that the method is POST method
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        f = Flower(name=name, color=color)
        f.save()
        context = {
            'name': name,
            'color': color
        }
        # print(":::: name was '%s' color was '%s'" % (name, color))
        return render(request, 'sunflower/flower_form.html', context=context)


def list_flowers(request):
    fl = Flower.objects.all()
    context = {
        'flowers': fl
    }
    return render(request, 'sunflower/flower_list.html', context=context)
