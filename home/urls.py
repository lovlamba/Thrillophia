from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("tours", views.tours, name='tours'),
    path("reach", views.reach, name='reach'),
    path("brochure", views.contact, name='contact'),
    path("contact",views.contact, name='contact')
]