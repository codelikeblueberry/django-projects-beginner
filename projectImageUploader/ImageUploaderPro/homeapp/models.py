from django.db import models

# Create your models here.
class ImageData(models.Model):
    image_name = models.ImageField(upload_to="images")
    image_date_time = models.DateTimeField(auto_now_add=True)