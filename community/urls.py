from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('library/', include('library.urls')),
    path('members/', include('members.urls')),
]
