"""If you're using a different server and storage backend for file uploads
 in Django, you can still upload files without using models. Django provides
   the FileSystemStorage class, which can be configured to use a different 
   server or storage backend. Here's a brief example:

Assuming you are using Amazon S3 as your storage backend, you would configure
 it in your settings.py:"""

# settings.py

AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
AWS_STORAGE_BUCKET_NAME = 'your_s3_bucket_name'
AWS_S3_REGION_NAME = 'your_s3_region_name'  # e.g., 'us-east-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


"""With this configuration, Django will use Amazon S3 as the storage backend.

Now, you can use the following example in your views to upload files without 
models:"""

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']

        # Specify the destination folder in your storage backend
        destination_folder = 'uploads/'

        # Construct the file path where the image will be saved
        destination_path = destination_folder + uploaded_file.name

        # Save the image to the storage backend
        storage = FileSystemStorage(location=destination_folder)
        storage.save(destination_path, uploaded_file)

        # You can perform additional actions here if needed

        return HttpResponse('Image uploaded successfully!')
    else:
        return render(request, 'your_app/your_form_template.html')



"""In this example, the FileSystemStorage class is used, but you can replace 
it with the appropriate storage backend for your server. The key is to set
 up the storage backend in your settings and then use it in your views to 
 save the files.

Ensure you have the necessary packages installed, such as boto3 and
 django-storages, based on your chosen storage backend. Adjust the 
 settings and view code accordingly for the specific storage backend
   you are using."""
