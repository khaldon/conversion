from django.urls import path

from . import views

urlpatterns = [
    path("html_2_pdf/", views.html2pdf, name="html2pdf"),
    path("docx_2_html/", views.docx2html, name="docx2html"),
    path("video_2_avi/", views.video2avi, name="video2avi"),
    path("video_2_mp3/", views.video2mp3, name="video2mp3"),
    path("video_2_mp4/", views.video2mp4, name="video2mp4"),
    path("video_2_flv/", views.video2flv, name="video2flv"),
    path("file/<str:out_path>/<str:filename>", views.file_download, name="file"),
    path("", views.HomePage.as_view(), name="home"),
    path("all_tools/", views.AllTools.as_view(), name="all_tools"),
]
