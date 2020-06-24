from django.http import Http404
from django.shortcuts import render

from .models import Farm, Division

# Create your views here.


def home(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        context = {"farms": Farm.objects.filter(farm_name__icontains=query)}
        return render(request, "home.html", context)
    else:
        context = {"farms": None}
        return render(request, "home.html", context)


def farms(request):

    context = {"farms": Farm.objects.all()}
    return render(request, "farms/farms.html", context)


def farm(request, farm_id):
    try:
        farm = Farm.objects.get(pk=farm_id)
    except Farm.DoesNotExist:
        raise Http404("Farm does not exist")
    context = {"farm": farm}
    return render(request, "farms/farm.html", context)


def divisions(request):

    context = {"divisions": Division.objects.all()}
    return render(request, "divisions/divisions.html", context)


def division(request, division_id):
    try:
        division = Division.objects.get(pk=division_id)
    except Farm.DoesNotExist:
        raise Http404("Division does not exist")
    context = {"division": division}
    return render(request, "divisions/division.html", context)
