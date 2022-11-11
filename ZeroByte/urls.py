from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Feed/', include('Feed.urls')),
    path('admin/', admin.site.urls),
]
