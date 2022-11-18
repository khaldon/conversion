from django.urls import path

from .views import HomePage, html2pdf, docx2html

urlpatterns = [
    path("html_2_pdf/", html2pdf, name="html2pdf"),
    path("docx_2_html/", docx2html, name="docx2html"),
    path("", HomePage.as_view(), name="home"),
]
