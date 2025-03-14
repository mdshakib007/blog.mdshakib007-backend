from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/api/v1/', admin.site.urls),
    path('api/v1/blog/', include('blog.urls')),
]
