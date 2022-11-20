from django.urls import path

from . import views

urlpatterns = [
    path("html_2_pdf/", views.html2pdf, name="html2pdf"),
    path("docx_2_html/", views.docx2html, name="docx2html"),
    path("file/<str:out_path>/<str:filename>", views.file_download, name="file"),
    path("", views.HomePage.as_view(), name="home"),
    path("all_tools/", views.AllTools.as_view(), name="all_tools"),
]
