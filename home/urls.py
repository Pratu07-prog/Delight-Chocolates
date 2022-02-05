from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Delight Chocolates Admin"
admin.site.site_title = "Delight Chocolates Admin Portal"
admin.site.index_title = "Welcome to Delight Chocolates"

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path("contact", views.contact, name = 'contact'),

]