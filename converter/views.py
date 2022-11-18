from django.shortcuts import render

from .handle import handle_html2pdf, handle_docx2pdf
from .forms import FileForm
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home.html"


def docx2html(request):
    if request.method == "POST":
        _docx2html = FileForm(request.POST, request.FILES)
        if _docx2html.is_valid():
            handle_docx2pdf(request.FILES["file"], "docx", "html")
            file_name = request.FILES["file"]
            return render(request, "converter/docx2html/docx2html.html")
        else:
            return render(request, "converter/error.html")
    else:
        _docx2html = FileForm()
        return render(
            request, "converter/docx2html/docx2html.html", {"form": _docx2html}
        )


def html2pdf(request):
    if request.method == "POST":
        _html_to_pdf = FileForm(request.POST, request.FILES)
        if _html_to_pdf.is_valid():
            handle_html2pdf(request.FILES["file"], "html", "pdf")
            file_name = request.FILES["file"]
            return render(
                request,
                "converter/html2pdf/html2pdf.html",
                {"file": str(file_name).replace("html", "pdf")},
            )
        else:
            return render(
                request,
                "converter/error.html",
            )
    else:
        _html_to_pdf = FileForm()
        return render(
            request, "converter/html2pdf/html2pdf.html", {"form": _html_to_pdf}
        )
