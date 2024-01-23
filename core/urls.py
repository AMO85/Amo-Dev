from django.urls import path
from .views import home
from django.conf import settings
from django.contrib import admin




urlpatterns = [
    # paths core
    path('', home, name="home"),
    # paths admin
    path('admin', admin.site.urls),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)