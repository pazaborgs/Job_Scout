from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', include('empresas.urls')),
    path('jobs/', include('jobs.urls')),
    path('', include('accounts.urls')),
    path('services/', include('services.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
