from django.urls import path
from homeapp import views
from django.conf.urls.static import static
from django.conf import settings

nonStaticURL = [

    path('home/',views.index,name='homepage')
] 

StaticURL = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns = nonStaticURL + StaticURL