"""webapp URL Configuration
Django doesn’t know what to do with the index.html
file we just created.
we’re going to associate the root directory (/)
with the newly created index.html.
"""
from django.conf.urls import url
from django.contrib import admin

from collection import views

urlpatterns = [
    url('', views.index, name='home'),
    url('admin/', admin.site.urls),
]
