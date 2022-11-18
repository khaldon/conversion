import os
import pdfkit
import aspose.words as aw


def main_handle_file(f, type_convert_from, type_convert_to):
    path_file = os.getcwd() + "/media/" + f.name
    out_path = (
        os.getcwd() + "/media/pdf/" + f.name.replace(type_convert_from, type_convert_to)
    )
    with open(path_file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path_file, out_path


def handle_html2pdf(f, type_convert_from, type_convert_to):
    """
    Parameters:

    (f): is a file paramter that pass request.FILES["file"]
    (type_convert_from): is a type of file that you will convert from
    (type_convert_to): is a type of file that you will convert to (the output file)

    """
    handle_file = main_handle_file(f, type_convert_from, type_convert_to)

    pdfkit.from_file(
        handle_file[0], handle_file[1], options={"enable-local-file-access": ""}
    )


def handle_docx2pdf(f, type_convert_from, type_convert_to):
    handle_file = main_handle_file(f, type_convert_from, type_convert_to)
    doc = aw.Document(handle_file[0])
    doc.save(handle_file[1])
