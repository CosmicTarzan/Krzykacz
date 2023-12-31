from django.contrib import admin
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('blog.urls')),
    path("register/", user_views.register, name='register'),
]