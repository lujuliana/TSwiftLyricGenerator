from django.contrib import admin
from django.urls import path
from generator.views import generate_lyric

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generate_lyric, name='home'),
]