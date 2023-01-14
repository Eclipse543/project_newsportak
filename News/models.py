from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    video = models.FileField(upload_to="vid/", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_limit_description(self):
        return self.description[:100]

class NewsSlider(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Sport(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Politic(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title