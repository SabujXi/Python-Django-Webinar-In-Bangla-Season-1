from django.shortcuts import render

from django.http import HttpResponse

from sunflower.models import Flower, Garden


def hi(request):
    return HttpResponse("You said hi I said bye")

def index(r):
    return render(r, "sunflower/index.html")


def flower_crud(request):
    if request.method == "GET":
        gardens = list(Garden.objects.all())
        context = {
            'gardens': gardens
        }
        return render(request, 'sunflower/flower_form.html', context)

    else:  # assumes that the method is POST method
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        description = request.POST.get('description', '')
        gid = request.POST.get('gid', '0')
        f = Flower(name=name, color=color)
        f.description = description
        f.garden = Garden.objects.get(id=int(gid))
        f.save()
        context = {
            'name': name,
            'color': color,
            'description': description,
            'gid': gid,
            'gardens': list(Garden.objects.all())
        }
        # print(":::: name was '%s' color was '%s'" % (name, color))
        return render(request, 'sunflower/flower_form.html', context=context)


def garden_crud(request):
    if request.method == "GET":
        return render(request, 'sunflower/garden_form.html')
    else:  # assumes that the method is POST method
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        g = Garden(name=name)
        g.description = description
        g.save()
        context = {
            'name': name,
            'description': description
        }
        # print(":::: name was '%s' color was '%s'" % (name, color))
        return render(request, 'sunflower/garden_form.html', context=context)


def list_flowers(request):
    fl = Flower.objects.all()
    context = {
        'flowers': fl
    }
    return render(request, 'sunflower/flower_list.html', context=context)
