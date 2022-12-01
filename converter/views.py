from django.shortcuts import render
import os
from .handle import handle_html2pdf, handle_docx2html, handle_video2video
from .forms import FileForm
from django.views.generic import TemplateView
from django.http import HttpResponse
import time


class HomePage(TemplateView):
    template_name = "home.html"


class AllTools(TemplateView):
    template_name = "all_tools.html"


def file_download(request, out_path, filename):
    with open(out_path.replace("*", "/"), "rb") as f:
        data = f.read()
    response = HttpResponse(data, content_type="text/html")
    response["Content-Disposition"] = 'attachment; filename="{0}"'.format(filename)
    return response


def main_file_convert_handle(request, handle_func, filetype_out, filename_template):
    if request.method == "POST":
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            filename, filetype_in = os.path.splitext(str(request.FILES["file"]))
            path = handle_func(request.FILES["file"], filetype_in[1:], filetype_out)
            filename = filename + "." + filetype_out
            path = path[1].replace("/", "*")
            return render(
                request,
                "converter/{0}/{1}.html".format(filename_template, filename_template),
                {"path": path, "filename": filename},
            )
        else:
            return render(request, "converter/error.html")
    else:
        file_form = FileForm()
        return render(
            request,
            "converter/{0}/{1}.html".format(filename_template, filename_template),
            {"form": file_form},
        )


def docx2html(request):
    return main_file_convert_handle(request, handle_docx2html, "html", "docx2html")


def html2pdf(request):
    return main_file_convert_handle(request, handle_html2pdf, "pdf", "html2pdf")


def video2avi(request):
    return main_file_convert_handle(request, handle_video2video, "avi", "video2avi")


def video2mp3(request):
    return main_file_convert_handle(request, handle_video2video, "mp3", "video2mp3")


def video2mp4(request):
    return main_file_convert_handle(request, handle_video2video, "mp4", "video2mp4")


def video2flv(request):
    return main_file_convert_handle(request, handle_video2video, "flv", "video2flv")


def video2wav(request):
    return main_file_convert_handle(request, handle_video2video, "wav", "video2wav")
