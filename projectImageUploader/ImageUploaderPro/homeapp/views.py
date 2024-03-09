from django.shortcuts import render
from .forms  import ImageForm
from .models import ImageData

# Create your views here.
def index(request):
    if request.method == "POST":
        """request.POST: <QueryDict: {'csrfmiddlewaretoken': ['7tO7PE3pwdWSuKRIYgZyXyTBECenzp56agjyBXhXcsgSd5dISzPF3Tc3nZnQrqHe']}>"""
        filled_image_form = ImageForm(request.POST,request.FILES) #why wrote request.POST?  ^
        if filled_image_form.is_valid():
            filled_image_form.save()

    image_objects = ImageData.objects.all()
    empty_image_form = ImageForm()
    return render(request, template_name='home.html', context={"form": empty_image_form,"images":image_objects})
