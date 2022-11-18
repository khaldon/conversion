from django.shortcuts import render
from django.http import HttpResponse
from .forms import HtmlToPdfForm
import os
import pdfkit
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home.html"


def handle_html_to_pdf(f):
    path_file = os.getcwd() + "/media/" + f.name

    out_path = os.getcwd() + "/media/pdf/" + f.name.replace("html", "pdf")
    with open(path_file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    pdfkit.from_file(path_file, out_path, options={"enable-local-file-access": ""})


def html_to_pdf(request):
    if request.method == "POST":
        _html_to_pdf = HtmlToPdfForm(request.POST, request.FILES)
        if _html_to_pdf.is_valid():
            handle_html_to_pdf(request.FILES["file"])
            file_name = request.FILES["file"]
            return render(
                request,
                "converter/htmltopdf/fileupload.html",
                {"file": str(file_name).replace("html", "pdf")},
            )
        else:
            return render(
                request,
                "converter/error.html",
            )
    else:
        student = HtmlToPdfForm()
        return render(request, "converter/htmltopdf/fileupload.html", {"form": student})
