from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addnews/", views.addnews, name="addnews"),
    path("details/<slug>", views.details, name="details"),
    path("sliderdetails/<slug>", views.slider_details, name="sliderdetails"),
    path("sportdetails/<slug>", views.sport_details, name="sportdetails"),
    path("politicdetails/<slug>", views.politic_details, name="politicdetails"),
    path("catdetails/<slug>", views.catDetails, name="catdetails"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]
