from django.urls import path
from .views import home, contact
from django.conf import settings
from django.contrib import admin




urlpatterns = [
    # paths core
    path('', home, name="home"),
    path('contact', contact, name="contact"),
    # paths admin
    path('admin', admin.site.urls),


]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)