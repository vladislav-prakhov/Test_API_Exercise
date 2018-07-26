from django.contrib import admin

# Register your models here.
from .models import FacePhoto

# class PostAdmin(admin.ModelAdmin):
#	pass


class FacePhotoModelAdmin(admin.ModelAdmin):
    list_display = ["user_name", "photo", "threshold", "res_n"]
    list_display_links = ["user_name"]
    class Meta:
        model = FacePhoto


admin.site.register(FacePhoto, FacePhotoModelAdmin)
