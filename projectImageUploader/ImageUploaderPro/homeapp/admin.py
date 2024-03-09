from django.contrib import admin
from.models import ImageData
# Register your models here.
@admin.register(ImageData)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image_name','image_date_time']
    
