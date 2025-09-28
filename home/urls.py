from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"), 
    path("privacy/", views.privacy, name="privacy"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("contact/", views.contact, name="contact"),
    path("copyright/", views.copyright_notice, name="copyright"),
]