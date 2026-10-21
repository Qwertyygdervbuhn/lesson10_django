from django.contrib import admin
from django.urls import path
from pages.views import about  # Импортируем нашу функцию из папки pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),  # Путь для страницы about
]
