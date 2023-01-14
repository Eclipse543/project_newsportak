from django.shortcuts import redirect, render

from .models import *


def index(request):
    data = {
        "postNews": Post.objects.all(),
        "sliderNews": NewsSlider.objects.all(),
        "sportNews":Sport.objects.all(),
        "politicNews":Politic.objects.all(),

    }
    return render(request, "News/index.html", data)


def details(request, slug):
    data = {"post": Post.objects.get(slug=slug)}
    return render(request, "News/details/details.html", data)

def slider_details(request, slug):
    data = {"slider": NewsSlider.objects.get(slug=slug)}
    return render(request, "News/details/sliderdetails.html", data)

def sport_details(request, slug):
    data = {"sport": Sport.objects.get(slug=slug)}
    return render(request, "News/details/sportdetails.html", data)

def politic_details(request, slug):
    data = {"politic": Politic.objects.get(slug=slug)}
    return render(request, "News/details/politicdetails.html", data)

def catDetails(request, slug):
    data = {"category": Category.objects.get(slug=slug)}
    return render(request, "News/details.html", data)


def addnews(request):
    if request.method == "POST":
        category = request.POST.get("category")
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        date = request.POST.get("date")
        image = ""
        if request.FILES:
            image = request.FILES["image"]
        description = request.POST.get("description")
        video = ""
        if request.FILES:
            video = request.FILES["video"]
            news = Post(
                title=title,
                slug=slug,
                date=date,
                image=image,
                description=description,
                video=video,
                category=Category.objects.get(slug=category),
            )
            news.save()
        back = request.META["HTTP_REFERER"]
        return redirect(back)
    else:
        return render(request, "News/addnews.html")


def contact(request):
    return render(request, "News/contact/contact.html")


def about(request):
    return render(request, "News/about/about.html")


def data_pass(request):
    data = {
        "categoryData": Category.objects.all(),
    }
    return data
