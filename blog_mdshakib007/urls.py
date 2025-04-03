from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/subscription/', include('subscription.urls')),
]
