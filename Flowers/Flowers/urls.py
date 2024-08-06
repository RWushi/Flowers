from django.contrib import admin
from django.urls import path
from AdminPanel.admin import content_admin_site, nomenclature_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', content_admin_site.urls),
    path('nomenclature/', nomenclature_admin_site.urls),
]
