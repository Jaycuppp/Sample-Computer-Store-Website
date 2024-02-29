from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Website.urls")),
    path('Customers/', include("django.contrib.auth.urls")),
    path('Customers/', include("Customers.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "The Admin Page"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to the Website`s Admin Page" 