"""
import admin
"""
from django.contrib import admin
from django.utils.translation.trans_real import mark_safe

from .models import Category, Post, NewsSlider, Sport, Politic


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "title",
        "slug",
        "date",
        "image_tag",
        "description",
        "video_tag",
    )
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["category"]
    search_fields = ["title", "description"]

    # get the image in the admin page
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{}" width="50" height="50" />'.format(obj.image.url)
            )
        else:
            return ""

    # det the video in the admin page
    def video_tag(self, obj):
        if obj.video:
            return mark_safe(
                '<video src="{}" width="50" height="50" />'.format(obj.video.url)
            )
        else:
            return ""

@admin.register(NewsSlider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "date", "image_tag", "description")
    prepopulated_fields = {"slug": ("title",)}

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{}" width="50" height="50" />'.format(obj.image.url)
            )
        else:
            return ""



@admin.register(Sport)
class AdminSport(admin.ModelAdmin):
    list_display = ("title", "slug", "date", "image_tag", "description")
    prepopulated_fields = {"slug": ("title",)}

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{}" width="50" height="50" />'.format(obj.image.url)
            )
        else:
            return ""



@admin.register(Politic)
class AdminPolitic(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "date",
        "image_tag",
        "description",    )
    prepopulated_fields = {"slug": ("title",)}

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{}" width="50" height="50" />'.format(obj.image.url)
            )
        else:
            return ""

