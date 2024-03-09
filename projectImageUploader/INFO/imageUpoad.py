"""Certainly! You can handle image uploads in Django without using a model
 by directly saving the uploaded file to the server. Here's an example:"""

from django.shortcuts import render
from django.http import HttpResponse
from .  import ImageUploadForm  # To get the uploaded file here

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image file
            uploaded_image = request.FILES['image']

            # Specify the destination folder where you want to save the uploaded image
            destination_folder = 'uploads/'

            # Construct the file path where the image will be saved
            destination_path = destination_folder + uploaded_image.name

            # Save the image to the server using File Handler
            with open(destination_path, 'wb+') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            # You can perform additional actions here if needed

            return HttpResponse('Image uploaded successfully!')
    else:
        form = ImageUploadForm()

    return render(request, 'your_app/your_form_template.html', {'form': form})
