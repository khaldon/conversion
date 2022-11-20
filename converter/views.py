from django.shortcuts import render

from .handle import handle_html2pdf, handle_docx2html
from .forms import FileForm
from django.views.generic import TemplateView
from django.http import HttpResponse


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


def main_file_convert_handle(
    request, handle_func, filetype_in, filetype_out, filename_template
):
    if request.method == "POST":
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            path = handle_func(request.FILES["file"], filetype_in, filetype_out)
            filename = str(request.FILES["file"]).replace(filetype_in, filetype_out)
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

    return main_file_convert_handle(
        request, handle_docx2html, "docx", "html", "docx2html"
    )


def html2pdf(request):
    return main_file_convert_handle(request, handle_html2pdf, "html", "pdf", "html2pdf")
