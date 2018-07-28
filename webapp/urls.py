"""webapp URL Configuration
Django doesn’t know what to do with the index.html
file we just created.
we’re going to associate the root directory (/)
with the newly created index.html.
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    url('', views.index, name='home'),
    url('about/', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url('contact/', TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url('admin/', admin.site.urls),
]
