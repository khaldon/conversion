from django.urls import path

from .views import html_to_pdf, HomePage

urlpatterns = [
    path("html_to_pdf/", html_to_pdf, name="htmltopdf"),
    path("", HomePage.as_view(), name="home"),
]
